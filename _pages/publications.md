---
title: Publications
permalink: /publications/
classes: wide
---
{% for category in site.data.papers.categories %}
  <h2>{{category.heading}}</h2>
  <ol>
  {% for paper in category.pubs %}
    <li><strong>{{paper.title}}</strong>.
    <br>
    {% for author in paper.authors %}
      {% if forloop.last %}
        {{author}}.
    {% else %}
        {{author}},
    {% endif %}
    {% endfor %}
    <br>
    <em>{{paper.venue}}</em>, 
    {% if paper.volumeissue %}
      {{paper.volumeissue}},
    {% endif %}
    ({{paper.year}}).
    {% if paper.links %}
    <br>
      {% for link in paper.links %}
        [<a href="{{link.url}}">{{link.text}}</a>] 
      {% endfor %}
    {% endif %}
    <br><br></li>
  {% endfor %}
  </ol>
{% endfor %}

\* denotes equal contribution