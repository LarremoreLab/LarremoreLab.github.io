---
title: Press
permalink: /press/
toc: true
analytics:
  provider: "google-gtag"
  google:
    tracking_id: "UA-36889698-2"
    anonymize_ip: false 
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