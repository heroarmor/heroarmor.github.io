---
layout: page
title: projekte
permalink: /de/projects/
lang: de
translations:
  en: /projects/
  de: /de/projects/
description: Forschungsprojekte und ausgewählte Kursprojekte.
nav: true
nav_order: 3
display_categories: [forschung, kursprojekte]
---

<!-- German project cards: _projects/de/*.md with lang: de -->
<div class="projects">
  {% assign de_projects = site.projects | where: "lang", "de" %}
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = de_projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endfor %}
</div>
