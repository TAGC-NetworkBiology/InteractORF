import pandas as pd

class ProteinFilter:
    """
    Une classe pour filtrer les lignes d'un fichier CSV en fonction de la colonne 'Reviewed'
    et enregistrer le résultat dans un nouveau fichier CSV.

    Paramètres :
    - input_csv (str) : Le chemin du fichier CSV d'entrée contenant les données à filtrer.
    - output_csv (str) : Le chemin du fichier CSV de sortie où seront enregistrées les lignes filtrées.

    Méthodes :
    - filter_proteins():
      Charge le fichier CSV d'entrée, filtre les lignes pour les entrées 'reviewed',
      et enregistre le résultat dans le fichier CSV de sortie.
    """
    def __init__(self, input_csv, output_csv):
        """
        Initialise une nouvelle instance de la classe ProteinFilter.

        Paramètres :
        - input_csv (str) : Le chemin du fichier CSV d'entrée.
        - output_csv (str) : Le chemin du fichier CSV de sortie.
        """
        self.input_csv = input_csv
        self.output_csv = output_csv

    def filter_proteins(self):
        """
        Charge le fichier CSV initial, filtre les lignes pour les entrées 'reviewed',
        et enregistre le résultat dans un nouveau fichier CSV.
        """
        # Charger le CSV initial
        df = pd.read_csv(self.input_csv, sep='\t')

        # Filtrer les lignes pour les entrées 'reviewed'
        reviewed_df = df[df['Reviewed'] == 'reviewed']

        # Obtenir les entrées uniques dans la colonne 'Entry'
        unique_entries = reviewed_df['Entry'].unique()

        # Créer un nouveau DataFrame avec les entrées uniques et 'reviewed'
        result_df = df[df['Entry'].isin(unique_entries) & (df['Reviewed'] == 'reviewed')]

        # Enregistrer le nouveau CSV
        result_df.to_csv(self.output_csv, sep='\t', index=False)

if __name__ == "__main__":
    # Exemple d'utilisation de la classe
    input_csv_path = '01_Reference/idmapping_2024_01_16.csv'
    output_csv_path = '05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes_reviewed.csv'

    protein_filter = ProteinFilter(input_csv_path, output_csv_path)
    protein_filter.filter_proteins()
