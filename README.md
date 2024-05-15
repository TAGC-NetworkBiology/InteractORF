# InteractORF : predictions of human sORF functions from an interactome study

## Goal of the repository
This GitHub repository contains the instructions and material to reproduce the analysis of the interactome form tissue-specific small peptides (sPEPs). This project is divided into small segments of analysis, with instructions on how to run each separated analysis. 

To reproduce the analysis, you have to first, prepare the environments (see "Environment requierement" section below), then execute the analysis step by step (see "Documentation" file in each sub-part of the respository).

## Environment requierement
Tho run this analysis, python3 and R version 4.4.0 or more are requiered. 
Third-party softwares such as specific libraries requiered to run the code are specified in the documentetion of each analysis.

A containerized environment will be available at a later date. 

## Structure of the analysis

This respository have the folowing structure 

```
.
├── 01_SEP_contre_protéome_interactome_complet_monocytes
│   ├── 03_Script
│   │   ├── Analyse_meilleurs_domaines_PFAM.Rmd
│   │   ├── Filtrer_protéome_monocytes_only.py
│   │   ├── Filtrer_protéome_monocytes_reviewed_only.py
│   │   ├── Interactome_complet_monocytes.py
│   │   ├── main.py
│   │   ├── Proteome_complet_monocytes_domain.py
│   │   └── __pycache__
│   │       ├── Filtrer_protéome_monocytes_only.cpython-310.pyc
│   │       ├── Filtrer_protéome_monocytes_reviewed_only.cpython-310.pyc
│   │       ├── Interactome_complet_monocytes.cpython-310.pyc
│   │       └── Proteome_complet_monocytes_domain.cpython-310.pyc
│   └── 06_Documentation
│       ├── README.md
│       └── Résumé_analyse.md
├── 02_Localisation_transcripts_SEP_avec_domaines_partiels
│   ├── 03_Script
│   │   ├── Analyse_localisation_sORF_sur_transcripts.Rmd
│   │   └── Extraction_sORFs_sans_domaine_etudie.py
│   └── 06_Documentation
│       └── README.md
├── 03_Analyse_domaines_entierement_présents_dans_sORF
│   ├── 03_Script
│   │   ├── Analyse_domaines_entiers_dans_sORFs.Rmd
│   │   ├── Domaines_entiers_avec_ajustement_5aa.py
│   │   ├── Domaines_entiers_dans_sORFs.py
│   │   ├── Extraction_taille_domaines.py
│   │   ├── main.py
│   │   ├── __pycache__
│   │   │   ├── Domaines_entiers_avec_ajustement_5aa.cpython-310.pyc
│   │   │   ├── Domaines_entiers_dans_sORFs.cpython-310.pyc
│   │   │   ├── Extraction_taille_domaines.cpython-310.pyc
│   │   │   └── sORF_taille_domaines_prédits.cpython-310.pyc
│   │   └── sORF_taille_domaines_prédits.py
│   └── 06_Documentation
│       └── README.md
├── 04_Interactome_sORFs_clustering_95
│   ├── 03_Script
│   │   ├── comptage_binary_interactions.py
│   │   ├── Comptage_interactions_par_clusters.py
│   │   ├── Interactions_cluster_95.py
│   │   ├── main.py
│   │   ├── nouveau_interactome_dd.py
│   │   └── __pycache__
│   │       ├── Comptage_interactions_par_clusters.cpython-310.pyc
│   │       ├── Interactions_cluster_95.cpython-310.pyc
│   │       ├── nouveau_interactome_dd.cpython-310.pyc
│   │       └── pfam2go.cpython-310.pyc
│   └── 06_Documentation
│       └── README.md
├── 05_Enrichissement_GO
│   ├── 03_Script
│   │   ├── Analysis_functional_enrichments_domain_interactors.Rmd
│   │   ├── Analysis_functionnal_under_representation_domains_interactors.Rmd
│   │   ├── Analysis_functionnal_under_representation_slims_interactors.Rmd
│   │   ├── extraction_interacteurs_sans_doublons.py
│   │   ├── __pycache__
│   │   │   └── pfam2go.cpython-310.pyc
│   │   └── reactome_terms_simplification.py
│   └── 06_Documentation
│       └── README.md
├── 06_Analyses_slims_présents_dans_sORFs
│   ├── 03_Script
│   │   └── Analyse_slims_sORFs.Rmd
│   └── 06_Documentation
│       └── README.md
├── 07_OCG_interactome
│   ├── 03_Script
│   │   ├── Fromating_cns_from_ocg.py
│   │   ├── get_largest_connected_component.py
│   │   ├── main.py
│   │   ├── ORF_enrichment_in_OGC_clusters.py
│   │   ├── __pycache__
│   │   │   ├── get_largest_connected_component.cpython-310.pyc
│   │   │   └── sPEP_PPI_intercatome.cpython-310.pyc
│   │   └── sPEP_PPI_intercatome.py
│   └── 06_Documentation
│       └── README.md
└── 08_Analyse_inferred_functions
    ├── 03_Script
    │   ├── Analysis_inferred_functions_to_sPEPs.Rmd
    │   ├── Count_clusters_annotated.py
    │   ├── Count_infered_ifunctions.py
    │   └── Inferred_functions_analysis.R
    └── 06_Documentation
        └── README.md

```
Each analysis is independent from another, but we strongly encourage to run them all in the indicated order. Each sub-anylysis got its own documentation on how to be run, and the necessary files ofter come from the previous analysis.

For more information on the files formats or the aim of each sub-anylisis, see the corresonding documentation.
