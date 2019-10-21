---
title: Code & Data
permalink: /openscience/
classes: splash
header:
    overlay_color: "#000"
    overlay_filter: "0.2"
    overlay_image: /assets/images/writing_code.jpg
---

<div>
	{% for repo in site.data.code.repos %}
  <h2>{{repo.title}}</h2>
  {% if repo.image_path %}
	<figure>
		<a href=
            {% if repo.links[0].url contains "://" %}
              "{{ repo.links[0].url }}"
            {% else %}
              "{{ repo.links[0].url | relative_url }}"
            {% endif %}
            title="{{ repo.title }}"
        >
        <img class="thumb" src=
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
  {% for link in repo.links %}
    [<a href="{{link.url}}">{{link.text}}</a>]
  {% endfor %}
  </p>
	{% endfor %}
</div>
		