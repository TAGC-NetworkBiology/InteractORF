import pandas as pd
import os
from openpyxl import Workbook

class ProteinMatcher:
    """
    Classe pour matcher les protéines entre le fichier des monocytes et les ensembles de données de domaines protéiques,
    puis générer un fichier Excel avec les résultats.

    Paramètres :
    - monocytes_file_path (str) : Le chemin du fichier vers l'ensemble de données des monocytes au format CSV.
    - domain_file_directory (str) : Le répertoire contenant les ensembles de données de domaines protéiques au format CSV.
    """
    def __init__(self, monocytes_file_path, domain_file_directory):
        """
        Initialise la classe en chargeant les données des monocytes et en récupérant la liste des fichiers de domaines.

        Args:
        - monocytes_file_path (str): Le chemin du fichier des monocytes au format CSV.
        - domain_file_directory (str): Le répertoire contenant les fichiers de domaines.
        """
        self.monocytes_data = pd.read_csv(monocytes_file_path, sep="\t")
        self.domain_files = self._get_domain_files(domain_file_directory)

    def _get_domain_files(self, directory):
        """
        Récupère la liste des fichiers de domaines dans le répertoire spécifié.

        Args:
        - directory (str): Le répertoire contenant les fichiers de domaines.

        Returns:
        - List[str]: Liste des chemins vers les fichiers de domaines.
        """
        directory = os.path.abspath(directory)
        domain_files = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.lower().endswith(".csv")]
        return domain_files

    def _load_domain_data(self, domain_file):
        """
        Charge les données d'un fichier de domaine au format CSV.

        Args:
        - domain_file (str): Le chemin vers le fichier de domaine.

        Returns:
        - pd.DataFrame: Les données du fichier de domaine.
        """
        return pd.read_csv(domain_file, sep="\t")

    def find_common_proteins_with_domain(self, domain_file):
        """
        Trouve et renvoie les protéines communes entre les monocytes et un ensemble spécifique de données de domaines.

        Args:
        - domain_file (str): Le chemin vers le fichier de domaine.

        Returns:
        - Tuple[List[str], int]: Liste des protéines communes et le nombre total de protéines communes.
        """
        domain_data = self._load_domain_data(domain_file)
        monocytes_column = "Identifiant"
        domain_accession_column = "Accession"

        common_proteins = set(
            self.monocytes_data[monocytes_column]
            .loc[self.monocytes_data[monocytes_column].isin(domain_data[domain_accession_column])]
        )

        total_common_proteins = len(common_proteins)
        return list(common_proteins), total_common_proteins

    def generate_excel_file(self, output_file_path):
        """
        Génère un fichier Excel contenant les informations sur les protéines communes pour chaque ensemble de données de domaines.

        Args:
        - output_file_path (str): Le chemin vers le fichier Excel de sortie.
        """
        wb = Workbook()
        ws = wb.active
        ws.append(["Identifiant PF", "Nombre_de_proteines_communes", "Proteines_communes"])

        for domain_file in self.domain_files:
            domain_id = os.path.basename(domain_file).split("_")[0]
            common_proteins, total_common_proteins = self.find_common_proteins_with_domain(domain_file)
            ws.append([domain_id, total_common_proteins, ', '.join(common_proteins)])

        wb.save(output_file_path)
        print(f"Fichier Excel généré avec succès à {output_file_path}.")

if __name__ == "__main__":
    monocytes_file_path = "/home/slivak/Bureau/Interactome_sORF_monocytes/01_SEP_contre_protéome_interactome_complet_monocytes/01_Reference/Intéractome_monocyte.csv"
    domain_file_directory = "/home/slivak/Bureau/Interactome_sORF_monocytes/01_SEP_contre_protéome_interactome_complet_monocytes/01_Reference/PF_domain_non_interacting"
    output_excel_file_path = "/home/slivak/Bureau/Interactome_sORF_monocytes/01_SEP_contre_protéome_interactome_complet_monocytes/05_Output/interactome_monocytes"

    matcher = ProteinMatcher(monocytes_file_path, domain_file_directory)
    matcher.generate_excel_file(output_excel_file_path)
