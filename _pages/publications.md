---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<div class="section-tile">
<h2>Working Papers</h2>

<ol class="pub-list" reversed>
{% for post in site.publications reversed %}
  {% if post.wip %}
    {% include archive-single-pub.html %}
  {% endif %}
{% endfor %}
</ol>

</div>

<div class="section-tile section-tile--alt">
<h2>Published</h2>

<ol class="pub-list" reversed>
{% for post in site.publications reversed %}
  {% unless post.wip %}
    {% include archive-single-pub.html %}
  {% endunless %}
{% endfor %}
</ol>

</div>
