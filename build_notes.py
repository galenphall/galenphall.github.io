#!/usr/bin/env python3
"""Build the notes pages from Markdown files in notes/.

Usage:
  python3 build_notes.py

Markdown files whose names begin with "_" are treated as templates or drafts
and are not published. Generated HTML is written to notes/index.html and
notes/<slug>/index.html.
"""

from __future__ import annotations

import datetime as dt
import html
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
NOTES_DIR = ROOT / "notes"


@dataclass
class Note:
    title: str
    date: str
    slug: str
    summary: str
    source: Path
    body_html: str


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body = "\n".join(lines[index + 1 :]).strip()
            meta: dict[str, str] = {}
            for raw in lines[1:index]:
                if ":" not in raw:
                    continue
                key, value = raw.split(":", 1)
                meta[key.strip().lower()] = value.strip().strip('"').strip("'")
            return meta, body

    return {}, text


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "note"


def title_from_path(path: Path) -> str:
    stem = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    return stem.replace("-", " ").replace("_", " ").title()


def date_from_path(path: Path) -> str:
    match = re.match(r"^(\d{4}-\d{2}-\d{2})", path.stem)
    if match:
        return match.group(1)
    return dt.date.today().isoformat()


def formatted_date(value: str) -> str:
    try:
        date = dt.date.fromisoformat(value)
    except ValueError:
        return value
    return date.strftime("%B") + f" {date.day}, {date.year}"


def render_inline(text: str) -> str:
    parts = text.split("`")
    rendered: list[str] = []
    for index, part in enumerate(parts):
        if index % 2:
            rendered.append(f"<code>{html.escape(part)}</code>")
        else:
            rendered.append(render_links_and_bold(part))
    return "".join(rendered)


def render_links_and_bold(text: str) -> str:
    link_re = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
    output: list[str] = []
    position = 0

    for match in link_re.finditer(text):
        output.append(render_bold(text[position : match.start()]))
        label = render_bold(match.group(1))
        url = html.escape(match.group(2), quote=True)
        output.append(f'<a href="{url}">{label}</a>')
        position = match.end()

    output.append(render_bold(text[position:]))
    return "".join(output)


def render_bold(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def render_markdown(text: str) -> str:
    lines = text.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None

    def close_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{render_inline(' '.join(line.strip() for line in paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            output.append(f"</{list_type}>")
            list_type = None

    def start_list(kind: str) -> None:
        nonlocal list_type
        close_paragraph()
        if list_type != kind:
            close_list()
            output.append(f"<{kind}>")
            list_type = kind

    index = 0
    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()

        if not stripped:
            close_paragraph()
            close_list()
            index += 1
            continue

        if stripped.startswith("```"):
            close_paragraph()
            close_list()
            language = slugify(stripped[3:].strip()) if stripped[3:].strip() else ""
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            class_name = f' class="language-{language}"' if language else ""
            output.append(f"<pre><code{class_name}>{html.escape(chr(10).join(code))}</code></pre>")
            continue

        if stripped.startswith("$$"):
            close_paragraph()
            close_list()
            math_lines = [raw]
            if stripped == "$$" or not stripped.endswith("$$"):
                index += 1
                while index < len(lines):
                    math_lines.append(lines[index])
                    if lines[index].strip().endswith("$$"):
                        break
                    index += 1
            output.append(f"<p>{html.escape(chr(10).join(math_lines))}</p>")
            index += 1
            continue

        heading = re.match(r"^(#{1,5})\s+(.+)$", stripped)
        if heading:
            close_paragraph()
            close_list()
            level = min(len(heading.group(1)) + 1, 6)
            output.append(f"<h{level}>{render_inline(heading.group(2))}</h{level}>")
            index += 1
            continue

        if re.match(r"^-{3,}$", stripped):
            close_paragraph()
            close_list()
            output.append("<hr>")
            index += 1
            continue

        unordered = re.match(r"^[-*]\s+(.+)$", stripped)
        if unordered:
            start_list("ul")
            output.append(f"<li>{render_inline(unordered.group(1))}</li>")
            index += 1
            continue

        ordered = re.match(r"^\d+[.)]\s+(.+)$", stripped)
        if ordered:
            start_list("ol")
            output.append(f"<li>{render_inline(ordered.group(1))}</li>")
            index += 1
            continue

        close_list()
        paragraph.append(raw)
        index += 1

    close_paragraph()
    close_list()
    return "\n".join(output)


def load_notes() -> list[Note]:
    notes: list[Note] = []
    NOTES_DIR.mkdir(exist_ok=True)

    for source in sorted(NOTES_DIR.glob("*.md")):
        if source.name == "README.md" or source.name.startswith("_"):
            continue

        meta, body = parse_front_matter(source.read_text(encoding="utf-8"))
        title = meta.get("title") or title_from_path(source)
        date = meta.get("date") or date_from_path(source)
        slug = slugify(meta.get("slug") or source.stem)
        summary = meta.get("summary", "")
        notes.append(
            Note(
                title=title,
                date=date,
                slug=slug,
                summary=summary,
                source=source,
                body_html=render_markdown(body),
            )
        )

    return sorted(notes, key=lambda note: (note.date, note.title), reverse=True)


def base_styles() -> str:
    return """body {
      max-width: 760px;
      margin: 2rem auto;
      padding: 0 1rem;
      color: #111;
      font-family: Georgia, "Times New Roman", Times, serif;
      font-size: 18px;
      line-height: 1.5;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      line-height: 1.2;
    }

    pre {
      overflow-x: auto;
    }

    img {
      max-width: 100%;
      height: auto;
    }

    li {
      margin-bottom: 0.75rem;
    }

    .item-title {
      font-weight: bold;
    }"""


def html_page(title: str, body: str, math: bool = False) -> str:
    mathjax = ""
    if math:
        mathjax = """
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [["$", "$"], ["\\\\(", "\\\\)"]],
        displayMath: [["$$", "$$"], ["\\\\[", "\\\\]"]]
      }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - Galen Hall</title>
  <style>
    {base_styles()}
  </style>{mathjax}
</head>
<body>
{body}
</body>
</html>
"""


def note_link(note: Note, prefix: str = "") -> str:
    date = html.escape(formatted_date(note.date))
    title = html.escape(note.title)
    url = f"{prefix}{note.slug}/"
    summary = f" {html.escape(note.summary)}" if note.summary else ""
    return f'<li><a class="item-title" href="{url}">{title}</a>. {date}.{summary}</li>'


def write_post(note: Note) -> None:
    note_dir = NOTES_DIR / note.slug
    note_dir.mkdir(parents=True)

    body = f"""  <nav><a href="../../">Home</a> / <a href="../">Notes</a></nav>
  <article>
    <h1>{html.escape(note.title)}</h1>
    <p>{html.escape(formatted_date(note.date))}</p>
{indent(note.body_html, 4)}
  </article>"""
    (note_dir / "index.html").write_text(html_page(note.title, body, math=True), encoding="utf-8")


def write_notes_index(notes: list[Note]) -> None:
    if notes:
        items = "\n".join(f"      {note_link(note)}" for note in notes)
        list_html = f"    <ol reversed>\n{items}\n    </ol>"
    else:
        list_html = "    <p>No notes yet.</p>"

    body = f"""  <nav><a href="../">Home</a></nav>
  <main>
    <h1>Notes</h1>
{list_html}
  </main>"""
    (NOTES_DIR / "index.html").write_text(html_page("Notes", body), encoding="utf-8")


def indent(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def main() -> None:
    notes = load_notes()
    for note in notes:
        write_post(note)
    write_notes_index(notes)
    print(f"Built {len(notes)} note(s).")


if __name__ == "__main__":
    main()
