import argparse
from sPEP_PPI_intercatome import Merge_sPEP_PPI_interactome
from get_largest_connected_component import get_largest_connected_component


def main(interaction_domain_domain, interaction_domain_motif, Canonical_protein_interactome):
    # File paths for Merge_sPEP_PPI_interactome
    sPEP_interactome = "05_Output/SPEP_interactome_monocytes.txt"
    merged_interactome = "05_Output/SPEPPI_PPI_interactome_monocytes.txt"

    # Call generate_associations method of Merge_sPEP_PPI_interactome
    merger = Merge_sPEP_PPI_interactome(interaction_domain_domain, interaction_domain_motif, sPEP_interactome, Canonical_protein_interactome, merged_interactome)
    merger.generate_associations()

    # File paths for get_largest_connected_component
    merged_interactome = '05_Output/SPEPPI_PPI_interactome_monocytes.txt'
    largest_connected_component = '05_Output/SPEPPI_PPI_interactome_monocytes_largest_connected_componant.ncol'

    # Call get_largest_connected_component function
    get_largest_connected_component(merged_interactome, largest_connected_component)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge interaction data and find largest connected component.")
    parser.add_argument("--interaction_domain_domain", default="01_Reference/dd_interactions_monocytes_cluster95.csv", help="Path to interaction domain domain CSV file")
    parser.add_argument("--interaction_domain_motif", default="01_Reference/dm_interactions_monocytes_SLiMpval001_ds04over80_cluster95.csv", help="Path to interaction domain motif CSV file")
    parser.add_argument("--Canonical_protein_interactome", default="01_Reference/PPI_MoonDB_UniProtAcc_monocytes.ncol", help="Path to canonical protein interactome NCOL file")
    args = parser.parse_args()

    main(args.interaction_domain_domain, args.interaction_domain_motif, args.Canonical_protein_interactome)

