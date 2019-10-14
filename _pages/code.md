---
title: Code
permalink: /code/
classes: wide
---

<div>
	{% for repo in site.data.code.repos %}
  <h3>{{repo.title}}</h3>
  {% if repo.image_path %}
	<figure>
		<a href=
            {% if repo.url contains "://" %}
              "{{ repo.url }}"
            {% else %}
              "{{ repo.url | relative_url }}"
            {% endif %}
            title="{{ repo.title }}"
        >
        <img class="thumb" height="300" width="300" src=
          {% if repo.image_path contains "://" %}
            "{{ repo.image_path }}"
          {% else %}
            "{{ repo.image_path | relative_url }}"
          {% endif %}
          alt="{{ repo.title }}">
        </a>
    </figure>
  {% endif %}
  <p>{{repo.description}}
    <br>
  [<a href="repo.url">link</a>]
  </p>
	{% endfor %}
</div>
		