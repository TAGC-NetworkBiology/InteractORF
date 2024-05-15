import pandas as pd
import os

class DomainesProcessor:
    """
    Classe pour le traitement des domaines dans les ORFs.

    Cette classe prend en entrée deux fichiers CSV : un fichier contenant les informations
    sur les domaines dans les ORFs (orf_domaines_file) et un fichier contenant les tailles
    réelles des domaines (tailles_domaines_pfam_file). Elle fusionne ces données, élimine
    les domaines dont la taille est inférieure à la taille réelle du domaine, et génère
    deux fichiers CSV en sortie : un pour les domaines éliminés et un pour les domaines
    entiers dans les sORFs.

    Paramètres :
    - orf_domaines_file (str): Chemin vers le fichier CSV contenant les informations sur les domaines dans les ORFs.
    - tailles_domaines_pfam_file (str): Chemin vers le fichier CSV contenant les tailles réelles des domaines.

    Méthodes :
    - process_domains(): Effectue le traitement des domaines, génère les fichiers CSV de sortie.
    """
    def __init__(self, orf_domaines_file, tailles_domaines_pfam_file):
        self.orf_domaines_df = pd.read_csv(orf_domaines_file)
        self.tailles_domaines_pfam_df = pd.read_csv(tailles_domaines_pfam_file, sep=',')

    def process_domains(self):
        """
        Traite les domaines dans les ORFs, élimine les domaines de taille inférieure à la taille réelle,
        et génère deux fichiers CSV en sortie.
        """
        # Supprimer les versions après le point dans la colonne 'ACC'
        self.tailles_domaines_pfam_df['ACC'] = self.tailles_domaines_pfam_df['ACC'].str.split('.').str[0]

        # Fusionner les DataFrames sur la colonne 'ACC'
        merged_df = pd.merge(self.orf_domaines_df, self.tailles_domaines_pfam_df,
                             left_on='signature', right_on='ACC', how='left')

        # Supprimer la colonne 'ACC'
        merged_df = merged_df.drop(columns=['ACC'])

        # Renommer la colonne 'Taille' en 'Taille_réelle_domaine'
        merged_df = merged_df.rename(columns={'Taille': 'Taille_réelle_domaine'})

        # Créer un DataFrame pour les domaines éliminés
        eliminated_domains_df = merged_df[merged_df['orf_length'] < merged_df['Taille_réelle_domaine']]
        eliminated_domains_df.to_csv('05_Output/domaines_éliminés.csv', index=False)

        # Créer un DataFrame pour les domaines entiers dans sORF
        entire_domains_df = merged_df[merged_df['orf_length'] >= merged_df['Taille_réelle_domaine']]
        entire_domains_df.to_csv('05_Output/domaines_entiers_dans_sORF.csv', index=False)

if __name__ == "__main__":
    # Ajoutez ici le chemin vers vos fichiers CSV
    orf_domaines_file_path = '05_Output/sORF_taille_domaines_prédits.csv'
    tailles_domaines_pfam_file_path = '05_Output/tailles_domaines_all_PFAM.csv'

    domains_processor = DomainesProcessor(orf_domaines_file_path, tailles_domaines_pfam_file_path)
    domains_processor.process_domains()
