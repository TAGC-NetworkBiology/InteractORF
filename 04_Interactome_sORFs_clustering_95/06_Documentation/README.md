**Modification of the interactome after localization of truncated domains and clusterisation**

**Overview**

This project aims to modifiy our simplify our initial interactome to make the analysis easier. In order to do this, the first step is to removing all of truncated domains that have been identified in 03_Analyse_domaines_entierement_présents_dans_sORFs. Then a clustering algorithm is used in order to supress all isoform sPEPs from the interactome, and a separate file is created to keep the number of interactions mediated by each sPEP of a cluster, allowing us to keep thoses interactions in mind for future analysis.   
This project allows us to create the new interactome, but the clustering need to be done separatly using a clustering algorithm, here we recommand using CD-Hit in order to have the same output as we did.

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
│   ├── dd_interactions_monocytes.csv
│   ├── dm_interactions_monocytes_SLiMpval001_ds04over80.csv
│   ├── domaines_entiers_dans_sORF_ajustement_5aa.csv
│   ├── Interactome_monocyte.csv
│   ├── ORFs_monocytes
│   │   ├── 3nNqgEK6SGV8Po2b.fasta
│   │   └── p0apeDMEnFNhhfA8.csv
│   ├── query_slims_SLiMpval001.csv
│   └── slims_ensemble_monocytes
├── 02_Container
├── 03_Script
│   ├── comptage_binary_interactions.py
│   ├── Comptage_interactions_par_clusters.py
│   ├── Interactions_cluster_95.py
│   ├── main.py
│   ├── nouveau_interactome_dd.py
├── 04_Workflow
├── 05_Output
│   ├── Clustering_95
│   │   ├── Cluster_orf_monocytes_95
│   │   ├── Cluster_orf_monocytes_95.clstr
│   │   ├── dd_interactions_monocytes_cluster95.csv
│   │   ├── dm_interactions_monocytes_SLiMpval001_ds04over80_cluster95.csv
│   │   └── interacteurs_slims_monocytes_cluster95.csv
│   ├── Comptages_interactions_par_clusters
│   │   ├── comptage_interactions_dd_par_prot.csv
│   │   ├── comptage_interactions_dm_par_prot.csv
│   │   ├── dd_interactions_cleaned.csv
│   │   └── dm_interactions_cleaned.csv
│   └── Interactions_dd_domaines_entiers_dans_sORFS
│       ├── interaction_dd_conservees.csv
│       └── interaction_dd_supprimees.csv
├── 06_Documentation
└── README.md
```

**Description**

The project consists of four Python scripts. 3 of thoses script are called in the main script. The tree first script allows for the analysis to run, the fourth script is just a simple tool to count the number of binary interaction from any file containg interaction between many porteins/sPEPs. Here is a short explaination of each script function : 

    nouveau_interactome_dd.py: This script eliminates truncated domains detected in the precedent step.
    interactions_cluster_95.py: This script eliminated all of the sPEP that are not the representative of a cluster from the interactome.
    comptage_interactions_par_clusters.py: This script stores in a separate file the number of interactions made by sORFs within the same cluster. 
    comptage_binary_interactions.py: This script is sepaated from the main part of this project. It's a simple tool that allows to count the number of binary interaction bewteen two sPEP/proteins from a cvs file.

**Dependencies**

    Python (>=3.6)
    Pandas


**Installation**

    Clone this repository to your local machine.
    Ensure you have Python installed on your system.
    Install the required dependencies using pip:

    pip install pandas

    You are now ready to use the scripts.


**Usage and data source**

In order to use this scripts, you need to have previously eliminated truncated domains (cf 03_Analyse_domaines_entierement_présents_dans_sORFs) and clusterised your proteins/sPEP. In this analysis the clustering algorithm used is CD-HIT, with the following command. You need to run the clustering and store the result (both files) in 05_Output/Clustering_95 .The use of a different clustering algorithm might aimpair the functionnality of the folowing scripts.

- Usage : 
    Navigate to the root of the directory.
    To run Cd-Hit, the command we used was the following, you can change the identity threshold (be sure to match the -n parametter according to CD-Hit documentation) to better suit your analysis.

    ``` bash
    cd-hit -i /home/slivak/Bureau/Interactome_sORF_monocytes/03_clustering_ORF_monocytes/01_Reference/ORFs_monocytes/3nNqgEK6SGV8Po2b.fasta -o /home/slivak/Bureau/Interactome_sORF_monocytes/03_clustering_ORF_monocytes/05_Output/Clustering_95/Cluster_orf_monocytes_95 -c 0.95 -n 5 -l 5
    ```
    Run the scripts with the folowing comande line command-line arguments. Refer to the individual script sections for details on arguments.

    ``` bash
    python3 03_Script/main.py
    ```
    View the generated output files in the specified output directories.

- Data source : 
    In order to run CD hit, we used the complete list of ORF  detected in monocytes in fasta format availaible of the MetamORF database (01_Reference/ORFs_monocytes/3nNqgEK6SGV8Po2b.fasta)

    In order to run thoses scripts, you need to have the folowing files : 
    - "domaine_entiers" : the list of non truncated domains (01_Reference/domaines_entiers_dans_sORF_ajustement_5aa.csv). This could be your own input or the result of the precedent step of the analysis. If you use your own file, the information needed are : orf_id,signature,orf_length,Taille_réelle_domaine,start_pos,end_pos,adjusted_start_pos,adjusted_end_pos,difference_taille_ajustée. 
    - "dd_interactions" : the output file from mimicint containing the predicted domain_domain interactions (01_Reference/dd_interactions_monocytes.csv).
    - "dm_interactions" : the output file from mimicint containing the predicted domain-motif interactions (01_Reference/dm_interactions_monocytes_SLiMpval001_ds04over80.csv). 
    - "SLiMs_list" : a list of all the slims prediected in your data (01_Reference/query_slims_SLiMpval001.csv). 
    - "clusters_orf" : the result of the clustering (output of CD-Hit) (05_Output/Clustering_95/Cluster_orf_monocytes_95).
    - "cluster_details" : the detailed results of the clustering (output file from CDhit ending with .clstr) (05_Output/Clustering_95/Cluster_orf_monocytes_95.clstr)

**Scripts Overview**
1. nouveau_interactome_dd.py    Dependencies

This script eliminates truncated domains from the interactome.

    Input Files:
        domaine_entiers: Path to the file containing non truncated domains.
        dd_interactions: Path to the file containing domain-domaine interaction data.
    Output Files:
        conserved_path: Path to the output file containing conserved interactions.
        deleted_path: Path to the output file containing deleted interactions.

2. interactions_cluster_95.py

This script creates a new interactome using representative ORFs of each cluster.

    Input Files:
        clusters_orf: Path to the file containing cluster data.
        dm_interactions: Path to the file containing domain-motif interaction data.
        conserved_path: Path to the file containing conserved interactions.
        SLiMs_list: Path to the file containing SLiMs data.
    Output Files:
        Output files are generated in the '05_Output/Clustering_95' directory.

3. comptage_interactions_par_clusters.py

This script stores the number of interactions made by sORFs within the same cluster.

    Input Files:
        conserved_path: Path to the file containing conserved interactions.
        dm_interactions: Path to the file containing interaction data.
        cluster_details: Path to the file containing cluster details.
    Output Files:
        Output files are generated in the '05_Output/Comptages_interactions_par_clusters' directory.

    
4. comptage_binary_interactions.py

This script count the number of binary interaction in an interaction file.
    Input File : 
        interaction_file_path: any csv that contains interactions between sPEPs and Proteins or Proteins/Proteins
    Output : 
        A text line indicating the number of binary interaction in your file.


**Contact**

SLIVAK Mathilde, stagiaire M2 - TAGC

Contact : mathilde.slivak@etu.univ-amu.fr