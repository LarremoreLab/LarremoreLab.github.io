---
title: Press
permalink: /press/
toc: true
---

{% for category in site.data.press.categories %}
  <h2>{{category.heading}}</h2>
  <ul>
  {% for item in category.press %}
    <li><a href="{{item.url}}" target="_blank">{{item.venue}}</a><br>
    {{item.author}}, {{item.date}}</li>
  {% endfor %}
  </ul>
{% endfor %}