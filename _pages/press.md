---
title: Press
permalink: /press/
toc: true
---

{% for category in site.data.press.categories %}
  <h2 id="{{category.heading}}">{{category.heading}}</h2>
  <ul>
  {% for item in category.press %}
    <li><a href="{{item.url}}" target="_blank">{{item.venue}}</a>, {{item.author}}, {{item.date}}.</li>
  {% endfor %}
  </ul>
{% endfor %}