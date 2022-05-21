---
title: Press
permalink: /press/
toc: true
---

{% for category in site.data.press.categories %}
  <h2 id="{{category.heading}}">{{category.heading}}</h2>
  <ul>
  {% for item in category.press %}
  {% if item.content %}
    {{item.content}}
  {% else %}
    <li><a href="{{item.url}}" target="_blank">{{item.venue}}</a>, {{item.author}}, {{item.date}}.</li>
  {% endif %}
  {% endfor %}
  </ul>
{% endfor %}