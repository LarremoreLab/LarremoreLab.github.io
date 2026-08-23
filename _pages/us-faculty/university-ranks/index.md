---
title: Quantifying hierarchy and dynamics in US faculty hiring and retention — university ranks
permalink: /us-faculty/university-ranks/
---

Explore the visualization below to see how universities rank in terms of prestige<sup><a href="#prestige-ranks">1</a></sup> or production<sup><a href="#production-ranks">2</a></sup>. This visualization supplements the *Nature* article [Quantifying hierarchy and dynamics in US faculty hiring and retention](https://www.nature.com/articles/s41586-022-05222-x). You can find links to the code and data used in that paper, as well as to another explorable visualization of how scholars move between universities when they become professors, [here](https://larremorelab.github.io/us-faculty/).

{% include us-faculty/university-ranks.html %}

<br>

<sup id="prestige-ranks">1</sup> A university's prestige rank is a measure of its ability to place its graduates as faculty at other prestigious universities. We use <a href="https://www.science.org/doi/10.1126/sciadv.aar8260">SpringRank</a> to infer prestige hierarchies across academia _in toto_ and, separately, in each domain and field. In order for a university to have a prestige rank in a given field, it must employ faculty in that field; doctoral universities that do not themselves employ faculty in that field are removed from the network before ranking.

<sup id="production-ranks">2</sup> A university's production rank is a measure of how many faculty it has trained. Production ranks are calculated for academia _in toto_ and, separately, for each domain and field. In order for a university to have a production rank in a given field, it must have trained at least one faculty member who is employed in that field.

The visualization covers 122 networks: academia, 10 domains, and 111 fields. Two of the domains (Public Administration & Policy; Media & Communication) and their fields were excluded from the analyses in the paper and are not in the public data files.

Copyright 2022–2026, Hunter Wapman & Daniel Larremore
