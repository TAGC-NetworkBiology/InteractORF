import os
import pandas as pd

# Spécifiez le chemin du dossier contenant les fichiers CSV
dossier_csv = '01_Reference/All_transcrpits_genes_interet'

# Spécifiez le chemin du fichier XLSX
fichier_xlsx = '05_Output/Domaines_interacting_transcripts_caractéristiques.xlsx'

# Spécifiez le chemin du dossier où vous souhaitez enregistrer les résultats
dossier_resultats = '05_Output'

# Créer le dossier de résultats s'il n'existe pas
os.makedirs(dossier_resultats, exist_ok=True)

# Charger le fichier XLSX dans un DataFrame
df_xlsx = pd.read_excel(fichier_xlsx)

# Créer un DataFrame vide pour stocker les résultats
df_global_resultats = pd.DataFrame()

for fichier_csv in os.listdir(dossier_csv):
    if fichier_csv.endswith('.csv'):
        chemin_fichier_csv = os.path.join(dossier_csv, fichier_csv)

        # Charger le fichier CSV dans un DataFrame
        df_csv = pd.read_csv(chemin_fichier_csv)

        # Identifier les lignes où 'MetamORF_orf_id' n'est pas dans 'ORF ID'
        lignes_sans_correspondance = df_csv[~df_csv['MetamORF_orf_id'].isin(df_xlsx['ORF ID'])]

        # Ajouter les résultats au DataFrame global
        df_global_resultats = pd.concat([df_global_resultats, lignes_sans_correspondance], ignore_index=True)

        print(f"Terminé pour {fichier_csv}.")

# Sélectionner les colonnes spécifiques
colonnes_specifiques = ['MetamORF_orf_id', 'MetamORF_transcript_id', 'transcript_id', 'transcript_name', 'rna_biotype', 'exp_count', 'orf_annotations']
df_global_resultats_selection = df_global_resultats[colonnes_specifiques]

# Enregistrer les résultats dans un seul fichier CSV
fichier_resultat_global = os.path.join(dossier_resultats, "sORF_genes_interet_sans_domaine_etudie.csv")
df_global_resultats_selection.to_csv(fichier_resultat_global, index=False)

print(f"Terminé. Résultats globaux enregistrés dans {fichier_resultat_global}")
