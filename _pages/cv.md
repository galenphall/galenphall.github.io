---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="section-tile">
<h2>Education</h2>

<div class="cv-entry">
<h3>Ph.D. in Physics and Sociology (Joint)</h3>
<div class="cv-entry__meta">University of Michigan, Ann Arbor &middot; 2023&ndash;Present</div>
<ul class="cv-entry__details">
<li>Pre-candidate for Ph.D.</li>
<li>GPA: 4.0</li>
<li>Courses: Social Theory 1 &amp; 2, Social Demography, Economic Sociology, Intro. to Adaptive Systems, Network Science, Econometrics 1 &amp; 2</li>
</ul>
</div>

<div class="cv-entry">
<h3>Sc.B. in Physics (Honors)</h3>
<div class="cv-entry__meta">Brown University &middot; 2016&ndash;2020</div>
<ul class="cv-entry__details">
<li>GPA: 3.93</li>
<li>Honors: Magna Cum Laude, Phi Beta Kappa, nominated for Sigma Xi</li>
</ul>
</div>

<div class="cv-entry">
<h3>Visiting Student</h3>
<div class="cv-entry__meta">Oxford University &middot; 2018&ndash;2019</div>
<ul class="cv-entry__details">
<li>GPA: 4.0 (converted)</li>
<li>Focus: Physics and Philosophy</li>
</ul>
</div>

</div>

<div class="section-tile section-tile--alt">
<h2>Work Experience</h2>

<div class="cv-entry">
<h3>Researcher (Full-time)</h3>
<div class="cv-entry__meta">Climate and Development Lab, Brown University &middot; March 2020&ndash;July 2023</div>
<ul class="cv-entry__details">
<li>Supervisor: Professor Timmons Roberts</li>
</ul>
</div>

<div class="cv-entry">
<h3>Researcher (Part-time)</h3>
<div class="cv-entry__meta">Climate and Development Lab, Brown University &middot; July 2019&ndash;March 2020</div>
<ul class="cv-entry__details">
<li>Supervisor: Professor Timmons Roberts</li>
</ul>
</div>

<div class="cv-entry">
<h3>Researcher (Part-time)</h3>
<div class="cv-entry__meta">The Ethics of Geoengineering Project, Harvard University &middot; June 2018&ndash;September 2018</div>
<ul class="cv-entry__details">
<li>Supervisor: Professor Lucas Stanczyk</li>
</ul>
</div>

<div class="cv-entry">
<h3>Researcher / Software Developer (Full-time)</h3>
<div class="cv-entry__meta">Brown Graphics Lab, Brown University &middot; March 2017&ndash;March 2018</div>
<ul class="cv-entry__details">
<li>Supervisor: Professor Andy Van Dam</li>
</ul>
</div>

</div>

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
<h2>Publications</h2>
<ol class="pub-list" reversed>
{% for post in site.publications reversed %}
  {% unless post.wip %}
    {% include archive-single-pub.html %}
  {% endunless %}
{% endfor %}
</ol>
</div>

<div class="section-tile">
<h2>Talks</h2>
<ol class="pub-list" reversed>
{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}
</ol>
</div>

<div class="section-tile section-tile--alt">
<h2>Grants</h2>

<div class="cv-entry">
<h3>NSF Graduate Research Fellowship <span class="grant-amount">$147,000</span></h3>
<div class="cv-entry__meta">2023</div>
<ul class="cv-entry__details">
<li>Fellowship funding three years of graduate school stipend and tuition</li>
</ul>
</div>

<div class="cv-entry">
<h3>CSSN Research Grant <span class="grant-amount">$26,000</span></h3>
<div class="cv-entry__meta">2021 &middot; PI: Galen Hall</div>
<ul class="cv-entry__details">
<li>Coauthors: Joshua Basseches (University of Michigan), Rebecca Bromley-Trujillo (Christopher Newport University)</li>
<li>Project: Research on climate policy and interest groups at the state level</li>
<li>Funding source: Climate Social Science Network (www.cssn.org)</li>
</ul>
</div>

<div class="cv-entry">
<h3>Brown University SPRINT Award <span class="grant-amount">$2,000</span></h3>
<div class="cv-entry__meta">2020 &middot; PI: Baylor Fox-Kemper</div>
<ul class="cv-entry__details">
<li>Project: Summer research extending undergraduate thesis results and preparing for academic article submission</li>
</ul>
</div>

</div>

<div class="section-tile">
<h2>Media Publications</h2>

<div class="cv-entry">
<h3>The faulty science, doomism, and flawed conclusions of Deep Adaptation</h3>
<div class="cv-entry__meta">2020 &middot; Published in OpenDemocracy</div>
<ul class="cv-entry__details">
<li>Co-authors: Thomas Nicholas and Colleen Schmidt</li>
<li>Critical response to "Deep Adaptation: A Map for Navigating Climate Tragedy"</li>
<li>Featured in The New York Times</li>
</ul>
</div>

</div>
