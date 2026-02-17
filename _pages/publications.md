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

## Working Papers

{% for post in site.publications reversed %}
  {% if post.wip %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Published

{% for post in site.publications reversed %}
  {% unless post.wip %}
    {% include archive-single.html %}
  {% endunless %}
{% endfor %}
