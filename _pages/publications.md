---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

---

## Preprints

<!-- {% for post in site.publications reversed %}
  {% if post.type == 'Preprint' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %} -->
<ul>
{% for post in site.publications reversed %}
  {% if post.type == 'Preprint' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}
</ul>
---

## Published 

<!-- {% for post in site.publications reversed %}
  {% if post.type == 'Accepted' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %} -->
<ul>
{% for post in site.publications reversed %}
  {% if post.type == 'Accepted' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}
</ul>


