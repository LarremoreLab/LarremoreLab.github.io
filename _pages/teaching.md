---
title: Teaching, Workshops, Recordings
permalink: /teaching/
classes: wide
header:
    overlay_color: "#000"
    overlay_filter: "0.2"
    overlay_image: /assets/images/flatirons1.jpg
---
{% for course in site.data.teaching.courses %}
  <h2>{{course.title}}</h2>
  <ul>
  {% for term in course.terms %}
    <li>{{term}}</li>
  {% endfor %}
  </ul>
{% endfor %}
