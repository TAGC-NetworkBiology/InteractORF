**Analyse du Protéome et Interactome complet des monocytes**
**Objectif**

L'objectif de ce projet est d'étudier les 10 meilleurs domaines PFAM les plus représentés chez les SEPs, comme définis dans la thèse de Sébastien A. CHOTEAU. L'analyse vise à comprendre comment ces domaines sont représentés dans le protéome et l'interactome des monocytes, en examinant s'il existe une utilisation préférentielle de ces domaines dans les SEPs.

**Structure du Répertoire**
/
|-- 01_Reference/
|   |-- PF_domain/
|   |-- rna_immune_cell.csv
|   |-- idmapping_2024_01_15.csv
|   |-- Intéractome_monocyte.csv
|-- 03_Script/
|    |-- Filtrer_données_protéome.py
|    |-- Filtrer_protéome_monocytes_reviewed_only.py
|    |-- Proteome_complet_monocytes_domain.py
|    |-- Interactome_complet_monocytes.py
|-- 05_Output/
|      |-- Résultats_intermédiaires/
|      |    |-- rna_immune_cell_monocytes.csv
|      |    |-- rna_immune_cell_monocytes_reviewed.csv
|      |-- proteome_monocytes_domains.xlsx
|      |-- interactome_monocytes_domains.xlsx
|-- 06_Documentation
|      |-- Résumé_analyses
|-- main.py
|-- README.md


**Prérequis**
    Python (version 3.6 ou supérieure)
    Pandas (version 1.3.3)
    openpyxl (version 3.0.18)


**Source des données** 
Le fichier Résumé_analyses.md dans le répertoire documentation reprend l'origine de toutes les données et les grandes lignes des objectifs derière chaque analyse.


**Étapes de l'Analyse**
Il est possible d'exécuter l'analyse d'un coup en utilisant le main, en se situant à la racine du projet 01_protéome_interactome_complet_monocytes et en rentrant la commande suivante :

```bash
python main.py
```

Il est également possible de réaliser l'expérience étape par étape, ce qui est recommandé si de nouveaux identifiants sont utilisés dans idmapping.

**Étape 1: Filtrer le Protéome des Cellules Immunitaires pour les Monocytes**

Exécutez le script Filtrer_données_protéome.py pour extraire les cellules immunitaires liées aux monocytes à partir du fichier rna_immune_cell.csv. Les résultats sont stockés dans 05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes.csv.

```bash

python 03_Script/01_protéome_interactome_complet_monocytes/Filtrer_données_protéome.py
```

**Étape 2 : Filtrer le Protéome des Monocytes pour les Protéines "Reviewed" Uniquement**

Exécutez le script Filtrer_protéome_monocytes_reviewed_only.py pour filtrer les protéines "reviewed" à partir du fichier idmapping_2024_01_15.csv. Les résultats sont stockés dans 05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes_reviewed.csv.

```bash

python 03_Script/01_protéome_interactome_complet_monocytes/Filtrer_protéome_monocytes_reviewed_only.py
```

**Étape 3 : Analyse du Protéome des Monocytes avec les Domaines Pfam**

Exécutez le script Proteome_complet_monocytes_domain.py pour analyser le protéome des monocytes avec les domaines Pfam. Les résultats sont stockés dans 05_Output/proteome_monocytes_domains.xlsx.

```bash

python 03_Script/01_protéome_interactome_complet_monocytes/Proteome_complet_monocytes_domain.py
```
**Étape 4 : Analyse de l'Interactome des Monocytes avec les Domaines Pfam**

Exécutez le script Interactome_complet_monocytes.py pour analyser l'interactome des monocytes avec les domaines Pfam. Les résultats sont stockés dans 05_Output/interactome_monocytes_domains.xlsx.
```bash

python 03_Script/01_protéome_interactome_complet_monocytes/Interactome_complet_monocytes.py
```
**Auteur** 

- SLIVAK Mathilde, stagiaire M2 - TAGC
Contact : mathilde.slivak@etu.univ-amu.fr
