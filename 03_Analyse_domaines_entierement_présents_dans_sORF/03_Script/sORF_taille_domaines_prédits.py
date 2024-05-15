import os
import pandas as pd

class sORF_taille_domaines_prédits:
    """
    Cette classe permet de traiter un fichier CSV contenant des données sur les ORFs et leurs domaines associés.
    Elle calcule la longueur des ORFs et génère un fichier CSV associant la taille des ORFs à leur signature Pfam.
    """

    def __init__(self, csv_file):
        """
        Initialise la classe en chargeant le fichier CSV spécifié.

        Parameters:
        - csv_file (str): Chemin vers le fichier CSV contenant les données ORF.
        """
        self.df = pd.read_csv(csv_file, delimiter='\t')

    def calculate_orf_length(self):
        """
        Calcule la longueur des ORFs en ajoutant une colonne 'orf_length' au DataFrame.
        """
        self.df['orf_length'] = self.df['end_pos'] - self.df['start_pos']

    def generate_pfam_length_csv(self):
        """
        Génère un fichier CSV associant la taille des ORFs à leur signature Pfam dans le dossier '05_Output'.
        La colonne 'orf_id' est également incluse dans le fichier final.
        """
        # Créer un nouveau DataFrame avec la signature, la taille et l'ID des ORFs associés
        result_df = self.df[['orf_id', 'signature', 'orf_length']]
        
        # Créer le chemin de sortie avec le dossier 05_Output
        output_folder = '05_Output'
        os.makedirs(output_folder, exist_ok=True)
        
        # Enregistrer le résultat dans un nouveau fichier CSV dans le dossier spécifié
        output_file_path = os.path.join(output_folder, 'sORF_taille_domaines_prédits.csv')
        result_df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # Ajoutez ici le chemin vers votre fichier CSV
    csv_file_path = '01_Reference/query_domains.csv'
    
    orf_processor = sORF_taille_domaines_prédits(csv_file_path)
    orf_processor.calculate_orf_length()
    orf_processor.generate_pfam_length_csv()