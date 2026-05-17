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

## Accepted Publications

{% for post in site.publications reversed %}
  {% if post.type == 'Accepted' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

---

## Preprints

{% for post in site.publications reversed %}
  {% if post.type == 'Preprint' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
