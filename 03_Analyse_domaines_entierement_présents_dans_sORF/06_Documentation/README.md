**Analyse du Protéome et Interactome complet des monocytes**
**Objectif**

L'objectif de cette analyse est de vérifier si les domaines trouvés par Sébastien Choteau sont réellement présents dans les sORFs ou s'ils sont tronqués (taille de la signature du domaine plus grande que l'alignement de ce domaine avec l'ORF). En effet, de nombreux domaines qu'il a retrouvé comme fortement représentés dans les SEPs sont en réalité partiellement présent, ce qui ne permet pas d'assumer qu'ils conservent leur fonction. Pour ce faire, nous avons dans un premier temps étudié si ces domaines sont totalement présent (un seul ORF possède une signature totale), puis nous avons autorisé un seuil de 5 acides aminés de chaque coté de la signature. 

**Structure du Répertoire**
/
|-- 01_Reference/
|   |-- Pfam-A.hmm
|   |-- spep_domains_mediating_int_df.csv
|-- 03_Script/
|    |-- Domaines_entiers_avec_ajustement_5aa.py
|    |-- Domaines_entiers_dans_sORFs.py
|    |-- Extraction_taille_domaines.py
|    |-- sORF_taille_domaines_prédits.py
|    |-- main.py
|-- 05_Output/
|      |-- domaines_eliminés_ap_ajustement_5aa.csv
|      |-- domaines_éliminés.csv
|      |-- domaines_entiers_dans_sORF_ajustement_5aa.csv
|      |-- domaines_entiers_dans_sORF.csv
|      |-- sORF_taille_domaines_prédits.csv
|      |-- tailles_domaines_all_PFAM.csv
|-- 06_Documentation
|-- README.md


**Prérequis**
    Python (version 3.6 ou supérieure)
    Pandas (version 1.3.3)


**Source des données** 
Le jeu de données utilisé pour connaitre la taille des signature des ORFs ont étés extraits depuis la base de données PFAM (téléchargement du fichier Pfam-A.hmm). La taille de l'alignement entre les sORFs et les domaines est extrait de l'analyse de Sébastien Choteau (alignement via InterproSan).

**Étapes de l'Analyse**

L'analyse peut être lancée directement depuis le terminal, à condition de se situer dans la racine de cette analyse (03_Analyse_domaines_entierement_présents_dans_sORF)

```Bash

python3 03_Script/main.py
```
**Étape 1: Extraire les identifiants et la taille de l'ensemble des signatures des domaines présents dans PFAM**
Le script 03_Script/Extraction_taille_domaines.py permet d'extraire l'ensemble de taille des signatures des domaines PFAM tel que présentes dans la base de données PFAM associée à l'identifiant PFAM correspondant. Ce script utilise le fichier 01_Reference/Pfam-A.hmm et le résultat est stocké dans 05_Output/tailles_domaines_all_PFAM.csv. 

**Étape 2 : Calul de la taille de l'alignement des ORFs sur les signature des domaines**
Le script 03_Script/sORF_taille_domaines_prédits.py permet de calculer la taille de l'alignement des ORFs sur les domaines de PFAM en utilisant l'ouput (modifié) de InterProScan produite par Sébastien Choteau (01_Reference/spep_domains_mediating_int_df.csv). Ce fichier à été extrait de son environnement R fourni dans le dossier mnt/project/InteractORF/Run/01_Monocytes_interactome/10_domain_and_slim_usage/2022_06_13_domain_and_slim_usage/08_output/RWorkspace_ImportData.RData
Le résultat est stocké dans le fichier 05_Output/sORF_taille_domaines_prédits.csv.

**Étape 3 : Récupération des domaines entièrement présents dans les sORFs**
Le script 03_Script/Domaines_entiers_dans_sORFs.py permet de stocker les sORFs possédant le domaine entier (taille de l'alignement = taille de la signature) dans le fichier 05_Output/domaines_entiers_dans_sORF.csv et ceux tronqués (taille de l'alignement < taille de la signature) dans le fichier 05_Output/domaines_éliminés.csv

**Étape 4 : Récupération des domaines présent dans les sORFs avec un seuil de +/- 10 acides aminés**
Le script 03_Script/Domaines_entiers_avec_ajustement_5aa.py permet de faire la même analyse qu'à l'étape 3 sauf que cette fois, une différence de 5 acide aminé au niveau du start et 5 acides aminés au niveau du stop est autorisée.Les résultats sont stockés dans 05_Output/domaines_entiers_dans_sORF_ajustement_5aa.csv pour les sORFs sont la taille de l'alignement est égales (+/- 10 aa) à la signature entière et les sORFs ne répondant pas à cette conditions sont stockés dans 05_Output/domaines_eliminés_ap_ajustement_5aa.csv



**Auteur** 
- SLIVAK Mathilde, stagiaire M2 - TAGC
Contact : mathilde.slivak@etu.univ-amu.fr
