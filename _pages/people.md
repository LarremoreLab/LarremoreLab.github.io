---
title: People
permalink: /people/
classes: wide
header:
    overlay_color: "#000"
    overlay_filter: "0.2"
    overlay_image: /assets/images/graduation2024.jpg
---

<div>
{% for person in site.data.people.people %}
    <figure>
    {% if person.url %}
        <a href=
            {% if person.url contains "://" %}
              "{{ person.url }}"
            {% else %}
              "{{ person.url | relative_url }}"
            {% endif %}
            title="{{ person.name }}"
        >
        <img class="thumb" src=
          {% if person.image_path contains "://" %}
            "{{ person.image_path }}"
          {% else %}
            "{{ person.image_path | relative_url }}"
          {% endif %}
          >
        </a>
    {% else %}
        <img class="thumb" src=
          {% if person.image_path contains "://" %}
            "{{ person.image_path }}"
          {% else %}
            "{{ person.image_path | relative_url }}"
          {% endif %}
          alt="{{ person.name }}">
    {% endif %}
    <figcaption>
        <strong>{{person.name}}</strong><br>
        {{person.title}}<br>
        {{person.subject}}
    </figcaption>
    </figure>
{% endfor %}
</div>

<div>
    <h3>Affiliated Researchers</h3>
    <ul>
{% for person in site.data.people.external %}
    {% if person.url %}
        <li><a href="{{ person.url}}" target="_blank">{{person.name}}</a>        
    {% else %}
        <li>{{person.name}}
    {% endif %}
    {% if person.title %}
        - {{person.title}}
    {% endif %}
    </li>
{% endfor %}
    </ul>
</div>

<div>
    <h3>Alumni</h3>
    
    <strong>Postdoctoral Fellows</strong>
    <ul>
{% for person in site.data.people.alumni.postdocs %}
    {% if person.url %}
        <li><a href="{{ person.url}}" target="_blank">{{person.name}}</a>        
    {% else %}
        <li>{{person.name}}
    {% endif %}
    {% if person.now %}
        ({{person.now}})
    {% endif %}
    </li>
{% endfor %}
    </ul>

    <strong>PhD Students</strong>
    <ul>
{% for person in site.data.people.alumni.phd_students %}
    {% if person.url %}
        <li><a href="{{ person.url}}" target="_blank">{{person.name}}</a>        
    {% else %}
        <li>{{person.name}}
    {% endif %}
    {% if person.now %}
        ({{person.now}})
    {% endif %}
    </li>
{% endfor %}
    </ul>

    <strong>MS Students</strong>
    <ul>
{% for person in site.data.people.alumni.ms_students %}
    {% if person.url %}
        <li><a href="{{ person.url}}" target="_blank">{{person.name}}</a>        
    {% else %}
        <li>{{person.name}}
    {% endif %}
    {% if person.now %}
        ({{person.now}})
    {% endif %}
    </li>
{% endfor %}
    </ul>

    <strong>Undergraduates</strong>
    <ul>
{% for person in site.data.people.alumni.undergraduates %}
    {% if person.url %}
        <li><a href="{{ person.url}}" target="_blank">{{person.name}}</a>        
    {% else %}
        <li>{{person.name}}
    {% endif %}
    {% if person.now %}
        ({{person.now}})
    {% endif %}
    </li>
{% endfor %}
    </ul>

    <strong>Past Affiliates</strong>
    <ul>
{% for person in site.data.people.alumni.affiliated %}
    {% if person.url %}
        <li><a href="{{ person.url}}" target="_blank">{{person.name}}</a>        
    {% else %}
        <li>{{person.name}}
    {% endif %}
    {% if person.now %}
        ({{person.now}})
    {% endif %}
    </li>
{% endfor %}
    </ul>

* joint with Aaron Clauset.
† joint with Sara Sawyer.
</div>