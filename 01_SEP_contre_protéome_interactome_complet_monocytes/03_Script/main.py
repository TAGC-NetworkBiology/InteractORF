# Script principal pour l'analyse du protéome et de l'interactome des monocytes

from Filtrer_protéome_monocytes_only import ImmuneCellFilter
from Filtrer_protéome_monocytes_reviewed_only import ProteinFilter
from Proteome_complet_monocytes_domain import ProteinMatcher
from Interactome_complet_monocytes import ProteinMatcher as InteractomeMatcher

def filter_immune_cells():
    """
    Étape 1: Filtrer le protéome des cellules immunitaires pour les monocytes.
    """
    input_prot_csv_path = '01_Reference/rna_immune_cell.csv'
    output_prot_csv_path = '05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes_non_interacting.csv'
    
    immune_cell_filter = ImmuneCellFilter(input_prot_csv_path, output_prot_csv_path)
    immune_cell_filter.filter_cells()

def filter_reviewed_proteins():
    """
    Étape 2: Filtrer le protéome des monocytes pour les protéines "reviewed" uniquement.
    """
    input_id_mapping_path = '01_Reference/idmapping_2024_01_16.csv'
    output_reviewed_csv_path = '05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes_reviewed.csv'
    
    protein_filter = ProteinFilter(input_id_mapping_path, output_reviewed_csv_path)
    protein_filter.filter_proteins()

def analyze_monocyte_proteome():
    """
    Étape 3: Analyse du protéome des monocytes avec les domaines Pfam.
    """
    prot_matcher = ProteinMatcher('05_Output/Résultats_intermédiaires/rna_immune_cell_monocytes_reviewed.csv', '01_Reference/PF_domain_non_interacting')
    prot_output_excel_path = '05_Output/proteome_monocytes_domains_non_interacting.xlsx'
    prot_matcher.generate_excel_file(prot_output_excel_path)

def analyze_monocyte_interactome():
    """
    Étape 4: Analyse de l'interactome des monocytes avec les domaines Pfam.
    """
    interact_matcher = InteractomeMatcher('01_Reference/Intéractome_monocyte.csv', '01_Reference/PF_domain_non_interacting')
    interact_output_excel_path = '05_Output/interactome_monocytes_domains_non_interacting.xlsx'
    interact_matcher.generate_excel_file(interact_output_excel_path)

if __name__ == "__main__":
    filter_immune_cells()
    filter_reviewed_proteins()
    analyze_monocyte_proteome()
    analyze_monocyte_interactome()
