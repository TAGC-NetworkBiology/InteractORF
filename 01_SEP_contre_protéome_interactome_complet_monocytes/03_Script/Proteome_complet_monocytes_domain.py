import pandas as pd
import os
from openpyxl import Workbook


class ProteinMatcher:
    """
    Une classe pour trouver les protéines communes entre les monocytes et les ensembles de données de domaines protéiques,
    et générer un fichier Excel avec les résultats.

    Paramètres :
    - monocytes_file_path (str) : Le chemin du fichier vers l'ensemble de données des monocytes au format CSV.
    - domain_file_directory (str) : Le répertoire contenant les ensembles de données de domaines protéiques au format CSV.

    Méthodes :
    - find_common_proteins():
      Recherche et renvoie les protéines communes entre les monocytes et chaque ensemble de données de domaines.

    - generate_excel_file(output_file_path: str):
      Génère un fichier Excel contenant les informations sur les protéines communes pour chaque ensemble de données de domaines.

    - find_common_proteins_with_domain(domain_file: str):
      Recherche et renvoie les protéines communes entre les monocytes et un ensemble spécifique de données de domaines.
    """   
    def __init__(self, monocytes_file_path, domain_file_directory):
        self.monocytes_data = pd.read_csv(monocytes_file_path, sep="\t")
        self.domain_files = self._get_domain_files(domain_file_directory)

    def _get_domain_files(self, directory):
        domain_files = []
        for filename in os.listdir(directory):
            if filename.endswith(".csv") and "_domain" in filename:
                domain_files.append(os.path.join(directory, filename))
        return domain_files

    def _load_domain_data(self, domain_file):
        return pd.read_csv(domain_file, sep="\t")

    def find_common_proteins(self):
        common_proteins = set()
        monocytes_uniprot_column = "Entry"
        domain_accession_column = "Accession"

        for domain_file in self.domain_files:
            domain_data = self._load_domain_data(domain_file)
            common_proteins.update(
                set(self.monocytes_data[monocytes_uniprot_column]).intersection(
                    set(domain_data[domain_accession_column])
                )
            )

        total_common_proteins = len(common_proteins)
        return list(common_proteins), total_common_proteins

    def generate_excel_file(self, output_file_path):
        wb = Workbook()
        ws = wb.active
        ws.append(["Identifiant PF", "Nombre _de_proteines_communes", "Protéines communes"])

        for domain_file in self.domain_files:
            domain_id = os.path.basename(domain_file).split("_")[0]
            common_proteins, total_common_proteins = self.find_common_proteins_with_domain(domain_file)
            ws.append([domain_id, total_common_proteins, ', '.join(common_proteins)])

        wb.save(output_file_path)

    def find_common_proteins_with_domain(self, domain_file):
        domain_data = self._load_domain_data(domain_file)
        monocytes_entry_column = "Entry"
        domain_accession_column = "Accession"

        common_proteins = set(
            self.monocytes_data[monocytes_entry_column]
        .   loc[self.monocytes_data[monocytes_entry_column].isin(domain_data[domain_accession_column])]
        )

        total_common_proteins = len(common_proteins)
        return list(common_proteins), total_common_proteins

if __name__ == "__main__":
    monocytes_file_path = "05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes_reviewed.csv"
    domain_file_directory = "/home/slivak/Bureau/Interactome_sORF_monocytes/01_SEP_contre_protéome_interactome_complet_monocytes/01_Reference/PF_domain_interacting"
    output_excel_file_path = "05_Output/proteome_monocytes_domains_non_interacting.xlsx"

    matcher = ProteinMatcher(monocytes_file_path, domain_file_directory)
    matcher.generate_excel_file(output_excel_file_path)



