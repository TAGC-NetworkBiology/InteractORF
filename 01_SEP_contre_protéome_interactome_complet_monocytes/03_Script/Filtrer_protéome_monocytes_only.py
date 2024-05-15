import pandas as pd

class ImmuneCellFilter:
    """
    Une classe pour filtrer les lignes d'un fichier CSV en fonction des cellules immunitaires spécifiées
    et enregistrer le résultat dans un nouveau fichier CSV.

    Paramètres :
    - input_csv (str) : Le chemin du fichier CSV d'entrée contenant les données à filtrer.
    - output_csv (str) : Le chemin du fichier CSV de sortie où seront enregistrées les lignes filtrées.

    Méthodes :
    - filter_cells():
      Charge le fichier CSV d'entrée, filtre les lignes pour les cellules immunitaires spécifiées,
      et enregistre le résultat dans le fichier CSV de sortie.
    """
    def __init__(self, input_csv, output_csv):
        """
        Initialise une nouvelle instance de la classe ImmuneCellFilter.

        Paramètres :
        - input_csv (str) : Le chemin du fichier CSV d'entrée.
        - output_csv (str) : Le chemin du fichier CSV de sortie.
        """
        self.input_csv = input_csv
        self.output_csv = output_csv

    def filter_cells(self):
        """
        Charge le fichier CSV initial, filtre les lignes pour les cellules immunitaires spécifiées,
        et enregistre le résultat dans un nouveau fichier CSV.
        """
        # Charger le CSV initial
        df = pd.read_csv(self.input_csv, sep='\t')

        # Filtrer les lignes pour les cellules immunitaires spécifiées
        immune_cells = ['classical monocyte', 'intermediate monocyte', 'non-classical monocyte', 'basophil', 'eosinophil', 'neutrophil']
        filtered_df = df[df['Immune cell'].isin(immune_cells)]

        # Enregistrer le nouveau CSV
        filtered_df.to_csv(self.output_csv, sep='\t', index=False)

if __name__ == "__main__":

    input_csv_path = '01_Reference/rna_immune_cell.csv'
    output_csv_path = '05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes.csv'

    immune_cell_filter = ImmuneCellFilter(input_csv_path, output_csv_path)
    immune_cell_filter.filter_cells()