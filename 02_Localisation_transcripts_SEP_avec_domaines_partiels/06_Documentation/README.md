**Analyse de la localisation des sORFS sur leurs transcripts**
**Objectif**

L'objectif de cette étude est d'étudier la localisation des ORFs portant les domaines pfam étudiés dans la partie 01_SEP_contre_protéome_interactome_complet_monocytes.
Les sORFs portant ces domaines ont été localisés sur des transcrpits en utilisant la base de données metamORF et les transcripts concernés ont ensuite été étudiés en utilisant Ensembl.
L'utilisation du script founi ne suffit pas à la réalisation complète de cette analyse.

**Structure du Répertoire**
02_Localisation_transcripts_SEP
  |-- 01_Reference/
      |-- All_transcripts_genes_interet/
          |-- ARPC2.csv
          |-- ARPC5.csv
          |-- CANX.csv
          |-- ENO1.csv  
          |-- IDO1.csv  
          |-- MGLL.csv
          |-- TPP1.csv
      |-- Analyse_seb_domain_interacting_usage/
          |-- 06_question06.html
      |-- Analyse_seb_domain_non_interacting_usage/
          |-- 06_question06.html
      |-- all_interactions_monocytes_SLiMpval001_ds04over80.csv
  |-- 03_Script/
      |-- Extraction_sORFs_sans_domaine_etudie.py
  |-- 05_Output/
      |-- .Rhistory
      |-- Analyse_localisation_sORF_sur_transcripts.html
      |-- Analyse_localisation_sORF_sur_transcripts.Rmd
      |-- Domaines_interacting_transcripts_caractéristiques.xlsx
      |-- Domaines_non_interacting_transcripts_caractéristiques.xlsx
      |-- sORF_genes_interet_sans_domaine_etudie.csv
      |-- sORF_gènes_interet_sans_domaine_etudie.csv
  |-- 06_Documentation/
      |-- Résumé_analyses

**Source des données** 
Le fichier Résumé_analyses.md dans le répertoire documentation reprend l'origine de toutes les données et les grandes lignes des objectifs derière chaque analyse.

**Étapes de l'Analyse**
Le scrpit python n'est pas suffisant pour faire tourner l'entiereté de l'analyse, qui nécéssite l'utilisation manuelle de certaines bases de données

**Etape 1: Extraction des identifiants des ORFs**
En connaissant les domaines Pfam des ORFs d'intéret (cf 01_01_SEP_contre_protéome_interactome_complet_monocytes), c'est à dire les ORFs possédant des domaines (participant ou non à des intéractions) surpreprésentés par rapport au protéome total des monocytes. Il est possible de récupérer leurs identifiants pour métamorph en utilisant le rapport de Sébastien CHOTEAU - Analyse_seb_domain_interacting_usage et Analyse_seb_domain_non_interacting_usage -

**Etape 2 : Extraction des informations pertinantes depuis les base de données**
Les fichiers Domaines_interacting_transcripts_caractéristiques.xlsx et Domaines_non_interacting_transcripts_caractéristiques.xlsx ressencent les informations prévelées manuellement depuis les base de données métamORF (utilisation des identifiants des ORFs) et Ensembl (utilisation des identifiant ENST issus de métamORF). Une analyse de ces résultats est proposée dans le fichier Analyse_localisation_sORF_sur_transcripts.html.

**Etape 3 : Etude des autres ORFs présent sur les gènes étudiés**
A ce jour, cette analyse n'a pas été finalisée suite à la réalisation que les orfs étudiés jusqu'à présent étaient en réalité des isoformes du même peptide. Il est possible d'étudier les autres orfs présents en utilisant les fichiers contenus dans 01_Reference/All_transcrpits_genes_interet, qui sont l'ensemble des ORfs présents sur les gènes d'interet extrait de métamorph. Le scrpit Extraction_sORFs_sans_domaine_etudie.py permet de retirer des fichiers les ORFs déjà étudiés (ceux portant les domaines sur-représentés), et permet la création du fichier sORF_genes_interet_sans_domaine_etudie.csv. 

**Auteur** 

- SLIVAK Mathilde, stagiaire M2 - TAGC
Contact : mathilde.slivak@etu.univ-amu.fr
