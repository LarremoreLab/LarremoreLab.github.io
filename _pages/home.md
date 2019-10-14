---
title: The Larremore Lab
layout: splash
permalink: /
header:
    overlay_color: "#000"
    overlay_filter: "0.2"
    overlay_image: /assets/images/mountains.jpg
excerpt: "Department of Computer Science<br>& BioFrontiers Institute<br>University of Colorado Boulder."
---

<h2>About the lab</h2>
<p>Our research focuses on developing methods of networks, dynamical systems, and statistical inference, to solve problems in social and biological systems. We try to keep a tight loop between data and theory, and learn a lot from confronting models and algorithms with real problems.

<p>In biological systems, we focus on the malaria parasite <em>P. falciparum</em> which evolves rapidly to evade the human immune system. Our goal is to understand the interplay between parasite evolution and human immunity, and its implications for parasite virulence, population structure, and epidemiology. 

<p>In social systems, we focus on understanding the  patterns and processes that define the ecosystem of scientific research and discovery. Our goal is to combine rigorous computation, ecological theory, and social science to understand how the scientific community can be made more equitable and more productive.

<h2>Lab News</h2>
<ul>
  {% for event in site.data.events %}
  <li>
    {% if event.date%}
      <b>{{event.date}} - </b>
    {% endif %}
    {{event.description}}
  </li>
  {% endfor %}
</ul>
