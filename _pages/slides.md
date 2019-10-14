---
title: Slides
permalink: /slides/
classes: wide
---

<div>
    {% for deck in site.data.slides.slides %}
    <figure>
        <a href=
            {% if deck.url contains "://" %}
              "{{ deck.url }}"
            {% else %}
              "{{ deck.url | relative_url }}"
            {% endif %}
            title="{{ deck.title }}"
        >
        <img class="thumb" width="300" src=
          {% if deck.image_path contains "://" %}
            "{{ deck.image_path }}"
          {% else %}
            "{{ deck.image_path | relative_url }}"
          {% endif %}
          alt="{{ deck.title }}">
        </a>
        <figcaption>
        {{deck.title}}
        </figcaption>
    </figure>
    {% endfor %}
</div>