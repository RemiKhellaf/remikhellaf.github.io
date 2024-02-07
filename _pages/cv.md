---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* MSc., Data Science for Business, Ecole Polytechnique, 2023
* Master in Management, HEC Paris, 2023

Work experience
======
* 2023: Reseacher and Data Scientist
  * Quinten Health

* 2022: Research Assistant
  * World Bank

* 2021: Consultant
  * Capgemini Invent

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Misc
======
<!-- * Music lover -->