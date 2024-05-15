**Functionnal enrichment of sPEP interactors**

**Overview**

This project aims to analyse the functionnal enrichment of sPEPs' interactors using results from gProfiler analysis. The functional enrichment have been done with multiples setting detailed bellow, using the online interface of gProfiler and most of the analysis have been done using R and the results are stocked in different rmarkdowns. 

**Contents**

    Repository structure
    Description
    Dependencies
    Installation
    Usage and data source
    Scripts Overview
    Contact

**Structure of the repository** 
```bash
.
├── 00_RawData
├── 01_Reference
│   ├── dd_interactions_monocytes_cluster95.csv
│   ├── dm_interactions_monocytes_SLiMpval001_ds04over80_cluster95.csv
│   ├── gProfiler_results
│   │   ├── gProfiler_hsapiens_27-02-2024 14-33-21__intersections.csv
│   │   ├── gProfiler_hsapiens_27-02-2024 14-38-40__intersections.csv
│   │   ├── gProfiler_hsapiens_27-02-2024 14-39-55__intersections.csv
│   │   ├── gProfiler_hsapiens_27-02-2024 14-43-22__intersections.csv
│   │   ├── gProfiler_hsapiens_27-02-2024 14-44-33__intersections.csv
│   │   ├── gProfiler_hsapiens_27-02-2024 14-46-45__intersections.csv
│   │   ├── gProfiler_hsapiens_28-02-2024 09-50-20__intersections.csv
│   │   └── gProfiler_hsapiens_28-02-2024 10-49-58__intersections.csv
│   ├── interacteurs_sORFs.csv
│   ├── interacteurs_sORFs_sans_doublons.csv
│   ├── Interactome_monocyte.csv
│   ├── liste_proteines_interactome_complet_monocytes_sans_doublons.csv
│   ├── liste_proteines_interagissant_avec_domaines_sORFs.csv
│   ├── liste_proteines_interagissant_avec_domaines_sORFs_sans_doublons.csv
│   ├── liste_proteines_interagissant_avec_slim_sORFs.csv
│   ├── liste_proteines_interagissant_avec_slim_sORFs_sans_doublons.csv
│   ├── ReactomePathwaysRelation.txt
│   └── ReactomePathways.txt
├── 02_Container
├── 03_Script
│   ├── extraction_interacteurs_sans_doublons.py
│   ├── __pycache__
│   │   └── pfam2go.cpython-310.pyc
│   └── reactome_terms_simplification.py
├── 04_Workflow
├── 05_Output
│   ├── Analysis_functional_enrichments_domain_interactors.html
│   ├── Analysis_functional_enrichments_domain_interactors.Rmd
│   ├── Analysis_functional_enrichment_slim_interactors.html
│   ├── Analysis_functional_enrichment_slim_interactors.Rmd
│   ├── Analysis_functionnal_under_representation_domains_interactors.html
│   ├── Analysis_functionnal_under_representation_domains_interactors.Rmd
│   ├── Analysis_functionnal_under_representation_slims_interactors.html
│   ├── Analysis_functionnal_under_representation_slims_interactors.Rmd
│   ├── Sipmified_REAC
│   │   ├── simplified_REAC_gProfiler_hsapiens_27-02-2024 14-33-21__intersections.csv
│   │   ├── simplified_REAC_gProfiler_hsapiens_27-02-2024 14-38-40__intersections.csv
│   │   ├── simplified_REAC_gProfiler_hsapiens_27-02-2024 14-39-55__intersections.csv
│   │   ├── simplified_REAC_gProfiler_hsapiens_27-02-2024 14-43-22__intersections.csv
│   │   ├── simplified_REAC_gProfiler_hsapiens_27-02-2024 14-44-33__intersections.csv
│   │   ├── simplified_REAC_gProfiler_hsapiens_27-02-2024 14-46-45__intersections.csv
│   │   ├── simplified_REAC_gProfiler_hsapiens_28-02-2024 09-50-20__intersections.csv
│   │   └── simplified_REAC_gProfiler_hsapiens_28-02-2024 10-49-58__intersections.csv
│   ├── slimGO_BP_associés_interacteurs_dd.csv
│   ├── slimGO_BP_associés_interacteurs_dm.csv
│   ├── slimGO_CC_associés_interacteurs_dd.csv
│   ├── slimGO_CC_associés_interacteurs_dm.csv
│   ├── slimGO_MF_associés_interacteurs_dd.csv
│   └── slimGO_MF_associés_interacteurs_dm.csv
├── 06_Documentation
└── README.md


```

**Description**
The project consists of 4 rmarkdown anlysis and two scripts allowing this analysis. Here os a short explaination of each script function : 

    extraction_interacteurs_sans_doublons.py: This script allows us to have a list of the interactors (cannonical protein interacting with sPEP) without duplicate in order to give the list to gProfiler.
    reactome_terms_simplification.py: This script aims at simplifing the enriched Reactome term using the hierchical classification of the terms.
    Analysis_functional_enrichment_slim_interactors.Rmd: This code allows us to analyse the output of gProfiler function enrichment concerning interctors of SLiMs (against all the monocyte proteome as well as the globality of the interactors)
    Analysis_functional_enrichment_domain_interactors.Rmd: This code allows us to analyse the output of gProfiler functional enrichment concerning interctors of domains (against all the monocyte proteome as well as the globality of the interactors)
    Analysis_functionnnal_under_representation_domain_interactors.Rmd: This code allows us to analyse the output of gProfiler functional under-representation concerning interctors of domains (against all the monocyte proteome as well as the globality of the interactors)
    Analysis_functionnal_under_representation_slim_interactors.Rmd: This code allows us to analyse the output of gProfiler functional under-representation concerning interctors of SLiMs (against all the monocyte proteome as well as the globality of the interactors)

**Dependencies**

    Python (>=3.6)
    Pandas
    R (>=4.3.3)
    BiocManager
    GSEA base

**Usage and data source**

In order to run this analysis, you need to first get the list of interctors without dupplicate. To do that, you can use the extraction_interacteurs_sans_doublons.py using your dd ou dm interaction file. 
The output of this script is stocked in 01/reference, and you can put this list in gProfiler (weither using the web interface or the many packages existing).

        The parameters from the gProfiler functional enrichment we used are the following : 
         -Background : either the whole monocyte proteome or the full list of the interactors depending on the biological question (cf html file for more biological explanation)
         -Threshold : 0.05
         -Correction : Benjamini-Hocheberg FDR

Usage : 

    Navigate to the root of the directory.
    First, get your interction file and if there is multiples interactions with the same protein, run the first script 'extraction_interacteurs_sans_doubons' in order to get a list of unique protein interacting with your sPEPs.

    Then, use gProfiler with the list of interactor, and the specific parameters you want according to your biological question. You need to downlowd the csv file output from the web interface (or stock the result in a varibale if your directly using the r package for exemple).

    If you want to study simplified GO and Reactome term, you need to downlowd the .obo file of SlimGO according to the GSEAbase documentation and add it to your file containing the package. You also need to downlowd the ReactomePathways.txt and ReactomePathwaysRelation.txt and run the reactome_terms_simplification.py script. 

    To visualyse the result of the functional enrichment, you can use the .RMD script, where you just need to modifiy the imput. In our case, each .RMD use 4 input :
        - The output of gProfiler when the enrichment have been performed of the full monocyte proteome background
        - The output of the reactome_terms_simplification.py for the same analyse
        - The output of gProfiler when the enrichment have been performed of the full interactors list background
        - The output of the reactome_terms_simplification.py for the same analyse

The output of each .Rmd contains for each result of gProfiler: 
        - A table with the full result of the gProfiler analysis
        - A visual representation of the 30 best GO:BP terms according to Fold Change
        - A table with the result of the simplified GO terms (Slim Go)
        - A visual representation of the Slim GO (GO:CC, GO:MF and GO:BP)
        - A visual representation of the 10 best Go categories (according to the percentage of presence of each Go category)
        - A visual representation Of 30 best Reactome term (according to Fold Change) 
        - A visual representation of the 10 best Reactome categories (according to the percentage of presence of each Reactome category)
        - A visual representation Of 30 best Wiki pathways terms (according to pvalue) 
        - A visual representation Of 30 best Huùan proteome ontology term (according to pvalue) 

**Contact**

SLIVAK Mathilde, stagiaire M2 - TAGC

Contact : mathilde.slivak@etu.univ-amu.fr