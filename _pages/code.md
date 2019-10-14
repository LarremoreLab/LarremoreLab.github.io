---
title: Open Science
permalink: /openscience/
classes: splash
header:
    overlay_color: "#000"
    overlay_filter: "0.2"
    overlay_image: /assets/images/writing_code.jpg
excerpt: "Find our code and data here"
---

<div>
	{% for repo in site.data.code.repos %}
  <h2>{{repo.title}}</h2>
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
		