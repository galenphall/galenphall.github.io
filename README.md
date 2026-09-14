# Galen Hall Website

This site is plain static HTML.

## Editing The Homepage

Edit `index.html` directly.

## Writing Notes

1. Copy `notes/_template.md` to a new file in `notes/`, for example `notes/2026-09-14-my-note.md`.
2. Edit the title, date, optional summary, and Markdown body.
3. Run:

```sh
python3 build_notes.py
```

The script rebuilds `notes/index.html` and each note page. The homepage links to the Notes page.

Markdown supports headings, paragraphs, links, bold text, lists, code fences, inline code, horizontal rules, and LaTeX math with `$...$` or `$$...$$`.
