---
title: Faculty Hiring Networks
permalink: /facultyhiring/
toc: true
---

![network](/assets/images/faculty_hiring.png)

A place to collect the reserach and data from faculty hiring network studies.

There are lots of studies on faculty hiring. They use a variety of different methods and have deep roots across various fields. This is just a place to see them all in one place.

{% for category in site.data.lit_facultyhiring.categories %}
  <h2>{{category.heading}}</h2>
  <ul>
  {% for item in category.publications %}
    <li><a href="{{item.url}}" target="_blank">{{item.title}}</a><br>
    {{item.authors}}, {{item.date}}</li>
  {% endfor %}
  </ul>
{% endfor %}