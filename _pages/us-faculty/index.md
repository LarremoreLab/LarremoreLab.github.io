---
title: Quantifying hierarchy and dynamics in US faculty hiring and retention
permalink: /us-faculty/
classes: wide
---

This page is a companion for the *Nature* article on faculty hiring and retention in US academia, written by [Hunter Wapman](https://www.hne.golf/), [Sam Zhang](https://sam.zhang.fyi), [Aaron Clauset](https://aaronclauset.github.io), and [Daniel Larremore](https://larremorelab.github.io/). It hosts visualizations of patterns in US faculty hiring, as well as links to deidentified data and replication code.

### Journal Reference
K. H. Wapman, S. Zhang, A. Clauset, and D. B. Larremore, "[Quantifying hierarchy and dynamics in US faculty hiring and retention]()." *Nature* 1(2), 345 (2022).

## Interactive Data Visualizations
<div>
    <figure>
        <a href="/us-faculty/hiring-flows/" title="hiring flows">
          <img class="thumb" width="300" src="/assets/images/us-faculty/hiring-flows.png" alt="a chord diagram of faculty hiring flows">
        </a>
        <figcaption>Explore how scholars<br>move between universities<br>when they become professors.</figcaption>
    </figure>
    <figure>
        <a href="/us-faculty/university-ranks/" title="university ranks">
          <img class="thumb" width="300" src="/assets/images/us-faculty/university-ranks.png" alt="a visualization of university ranks">
        </a>
        <figcaption>Explore how universities<br>rank, as measured by<br>prestige<sup><a href="#prestige-ranks">1</a></sup> or production<sup><a href="#production-ranks">2</a></sup>.</figcaption>
    </figure>
</div>

<sup id="prestige-ranks">1</sup> A university's prestige rank is a measure of its ability to place its graduates as faculty at other prestigious universities. We use <a href="https://www.science.org/doi/10.1126/sciadv.aar8260">SpringRank</a> to infer prestige hierarchies across academia _in toto_ and, separately, in each domain and field. In order for a university to have a prestige rank in a given field, it must employ faculty in that field and have trained at least one faculty member who is employed in that field.

<sup id="production-ranks">2</sup> A university's production rank is a measure of how many faculty it has trained. Production ranks are calculated for academia _in toto_ and, separately, for each domain and field. In order for a university to have a production rank in a given field, it must have trained at least one faculty member who is employed in that field.

### Data and Code

- data used in the paper: [github](https://github.com/LarremoreLab/us-faculty-hiring-networks) [zenodo](https://zenodo.org/record/6941651)
- code used in the paper: [github](https://github.com/LarremoreLab/us-faculty-hiring-and-retention-code) [zenodo](https://zenodo.org/record/6941612)


Copyright 2022, Hunter Wapman & Daniel Larremore
