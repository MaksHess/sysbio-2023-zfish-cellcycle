# sysbio-2023-zfish-cellcycle
Quantification of cell-cycle synchrony and mitotic waves in early stage zebrafish embryos.

## Introduction
<figure>
    <img src="images\early_zfish_development.png" title="text" width=1000px>
    <figcaption>Overwiev of early zebrafish development (adapted from Kimme et al. 1995)</figcaption>
</figure>

Early zebrafish development is dominated by fast cell divisions (cycling/blastula stage ; cycle ~ 1-9; divisions every 15 min) followed by the Mid Blastula Transition (MBT; around cycle 10) where cell cycle lengthens and becomes asynchronous
[(Kimmel et al. 1995)](https://anatomypubs.onlinelibrary.wiley.com/doi/epdf/10.1002/aja.1002030302).   
[Keller et al.](https://www.science.org/doi/10.1126/science.1162493?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed) collected live data of early development and describe three modes of mitotic waves, radial waves 
(cycle 1-9) followed by peripheral waves (cycle 9-13) and finally asynchronous patches (beyond cycle 13).

<figure>
    <img src="images\mitotic_waves.png" title="text" width=600px>
    <figcaption>Mitotic waves in early zfish development (Keller et al. 2008, Fig 4A)</figcaption>
</figure>

## Data
Features extracted from IF stained, fixed (cycle 7-13), SDC Microscopy data with a cell cycle model applied.  
Description of the .csv file:


| Feature                 | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| **roi**                 | site/embryo identifier (since there's one embryo per site in the imaging setup) |
| **label**               | nuclei id (from the labelimage; only unique when combined with roi column)      |
| **cycle**               | division cycle (rounded from log2_cell_count)                                   |
| **Centroid-[xyz]**      | centroid position in the site coordinate system                                 |
| **NormalizedCcp**       | cell cycle phase [0, 2pi)                                                       |
| **CentroidTrans-[xyz]** | centroid position in the site coordinate system                                 |


## Goals of the analysis
### Quantify global cell cycle synchrony per embryo
- [ ] **1** Use a metric like circular variance (`CircVar`) or mean resultant length (`CircR`) to quantify global asynchrony per embryo
### Quantify local cell cycle synchrony per embryo
- [ ] **2** Define local neighborhoods
  - [ ] **2a** Radius neighborhood
  - [ ] **2b** KNN neighborhood
  - [ ] **2c** Touch neighborhood (Delaunay)
- [ ] **3** Calculate the synchrony metric (**1**) in neighborhoods of differing sizes
- [ ] **4** Find a "lenght scale of synchrony" for each timepoint/cycle
- [ ] **5** Use the laplacian on connectivity graphs as an alternative approach to find said length scale
### Quantify mitotic waves by calculating gradients of CCP
- [ ] **6** Interpolate CCP on a grid to calculate the gradient
- [ ] **7** Use the laplacian on the touch neighborhood to get to the direction of mitotic waves
- [ ] **8** Use a graph based approach while retaining the centroid positions of each node
### Strech goal: Cell cycle modelling à la [this paper](https://www.sciencedirect.com/science/article/pii/S0960982204006943#FIG1)
- [ ] **9** Modelling of cycling nuclei with variable noise in the frequency/phase
  - [ ] **9a** Minimal cell cycle model (**Fig 1A**)
  - [ ] **9b** Spatial coupling / modelling of waves (?)
  - [ ] **9c** More advanced cell cycle model (**Fig 1B**)
