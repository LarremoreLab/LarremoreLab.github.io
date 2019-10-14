---
title: Publications
permalink: /publications/
classes: wide
---
<ol>
{% for paper in site.data.papers %}
  <li>{{paper.title}}.
  <br>
  {% for author in paper.authors %}
  	{% if forloop.last %}
    	{{author}}.
	{% else %}
  		{{author}},
	{% endif %}
  {% endfor %}
  <br>
  {{paper.venue}}, 
  {% if paper.volumeissue %}
    {{paper.volumeissue}},
  {% endif %}
  ({{paper.year}}).
  <br>
  {% for link in paper.links %}
  [<a href="{{link.url}}">{{link.text}}</a>] 
  {% endfor %}
  <br><br></li>
{% endfor %}
</ol>

\* denotes equal contribution