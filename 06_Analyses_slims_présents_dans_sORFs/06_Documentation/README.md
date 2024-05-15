**Analysis of Short Linear Motifs presents in sPEPs**

**Overview**
This R script performs analyses on small open reading frames (sORFs) present in monocytes. It utilizes predicted motifs from MimicINT to visualize the distribution of SLiMs (Short Linear Motifs) within these sORFs and provides insights into their characteristics.

**Contents**

    Repository structure
    Installation and Requirements
    Usage
    Description of Analyses
    Output
    Contact

**Repository structure**

```bash
.
├── 00_RawData
├── 01_Reference
│   ├── dm_interactions_monocytes_SLiMpval001_ds04over80_cluster95.csv
│   └── liste_SLIMs.csv
├── 02_Container
├── 03_Script
├── 04_Workflow
├── 05_Output
│   ├── Analyse_slims_sORFs.html
│   ├── Analyse_slims_sORFs.Rmd
│   └── liste_sORFs_slim.csv
├── 06_Documentation
└── README.md
```

**Installation and Requirements**

Ensure you have the following R packages installed:

    ggplot2
    dplyr

**Usage**

    Ensure your data is in CSV format. The imput need to be the output from MimicINT, here it's our domain-motif predicted interaction file after the clustering of the sORFs.
    Adjust the file path in the script to point to your CSV file.
    Run the script in R environment.

**Description of Analyses**
1. Histogram of SLiMs Present in sORFs

This section generates a histogram showing the distribution of SLiMs within sORFs. Each SLiM is color-coded based on its class.
2. Histogram of SLiM Classes in sORFs

Here, the script provides another histogram, this time displaying the distribution of SLiM classes within sORFs.

    CLV: Cleavage site
    DEG: Degradation site
    DOC: Docking site
    LIG: Ligand binding site
    MOD: Post translational modification site
    TRG: Targeting site

3. SLiM with the Highest Occurrence

This section identifies and presents the SLiMs with the highest occurrence within the dataset, along with their descriptions and associated functions (need to be ajusted by hand, the information in our output is comming from the ELM database). The top 10 SLiMs are listed.

**Outputs**

The script generates visualizations in HTML format for easy viewing and sharing.

    Histogram of SLiMs Present in sORFs
    Histogram of SLiM Classes in sORFs
    Table of SLiMs with the highest occurrence, their descriptions, and associated functions.

**Contact**

SLIVAK Mathilde, stagiaire M2 - TAGC

Contact : mathilde.slivak@etu.univ-amu.fr