---
title: Quantifying hierarchy and dynamics in US faculty hiring and retention
permalink: /us-faculty/
classes: wide
---

This page is a companion for the *Nature* [article](https://www.nature.com/articles/s41586-022-05222-x) *Quantifying hierarchy and dynamics in US faculty hiring and retention*, written by [Hunter Wapman](https://www.hne.golf/), [Sam Zhang](https://sam.zhang.fyi), [Aaron Clauset](https://aaronclauset.github.io), and [Daniel Larremore](https://larremorelab.github.io/). It hosts visualizations of patterns in US faculty hiring, links to deidentified data and replication code, and a record of [corrections and updates](#corrections-and-updates) to the paper and the data.

### Journal Reference
K. H. Wapman, S. Zhang, A. Clauset, and D. B. Larremore, "[Quantifying hierarchy and dynamics in US faculty hiring and retention](https://doi.org/10.1038/s41586-022-05222-x)." *Nature* **610**, 120–127 (2022).

K. H. Wapman, S. Zhang, A. Clauset, and D. B. Larremore, "[Author Correction: Quantifying hierarchy and dynamics in US faculty hiring and retention](https://doi.org/10.1038/s41586-023-06379-9)." *Nature* **619**, E49 (2023). See [corrections and updates](#corrections-and-updates) below.

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

<sup id="prestige-ranks">1</sup> A university's prestige rank is a measure of its ability to place its graduates as faculty at other prestigious universities. We use <a href="https://www.science.org/doi/10.1126/sciadv.aar8260">SpringRank</a> to infer prestige hierarchies across academia _in toto_ and, separately, in each domain and field. In order for a university to have a prestige rank in a given field, it must employ faculty in that field; doctoral universities that do not themselves employ faculty in that field are removed from the network before ranking.

<sup id="production-ranks">2</sup> A university's production rank is a measure of how many faculty it has trained. Production ranks are calculated for academia _in toto_ and, separately, for each domain and field. In order for a university to have a production rank in a given field, it must have trained at least one faculty member who is employed in that field.

The visualizations cover 122 networks: academia, 10 domains, and 111 fields. Two of the domains (Public Administration & Policy; Media & Communication) and their fields were excluded from the analyses in the paper and are not in the public data files.

### Data and Code

- data used in the paper: [github](https://github.com/LarremoreLab/us-faculty-hiring-networks) (latest: [v2026.08](https://github.com/LarremoreLab/us-faculty-hiring-networks/releases/tag/v2026.08)) · [zenodo](https://doi.org/10.5281/zenodo.6941650)
- code used in the paper: [github](https://github.com/LarremoreLab/us-faculty-hiring-and-retention-code) · [zenodo](https://doi.org/10.5281/zenodo.6941611)

The Zenodo links are concept DOIs and always resolve to the latest version of each record.

### Corrections and updates

**July 2023 — Author Correction to the paper.** The Methods section originally described two criteria for identifying new hires, but the analyses used one: faculty were labelled as new hires if they earned their degree within 4 years of their first recorded employment as faculty (59,007 new faculty, 20.0% of the faculty in the dataset). The text of the paper was corrected to match the analyses that were performed; the results are unchanged. [Author Correction, *Nature* **619**, E49 (2023)](https://doi.org/10.1038/s41586-023-06379-9).

**August 2026 — Update to the public data files.** The four data files in the [us-faculty-hiring-networks](https://github.com/LarremoreLab/us-faculty-hiring-networks) repository were regenerated from the original analysis pipeline — same underlying data, sample, and rankings — to fix several bugs in the step that exported them. In particular, about 2,800 ranked institutions were missing from `institution-stats.csv`, leaving gaps in the ordinal prestige ranks; attrition is now reported in two explicit units (faculty and faculty-years); the empirical `FractionUpHierarchyHires` in `stats.csv` was restored; 6,134 artifact rows were removed from `edge-lists.csv`; and the README was corrected. The full list is in the repository's [changelog](https://github.com/LarremoreLab/us-faculty-hiring-networks#changelog). We thank Todd Jones (Mississippi State University) and Alex Bell (Georgia State University) for finding and diagnosing the missing institutions. The interactive visualizations on this page were built directly from the pipeline and were not affected.

Copyright 2022–2026, Hunter Wapman & Daniel Larremore
