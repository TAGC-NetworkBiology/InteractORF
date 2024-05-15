import argparse
from nouveau_interactome_dd import interactome_sans_domaines_tronqués
from Interactions_cluster_95 import Interactome_cluster_95
from Comptage_interactions_par_clusters import Count_interactions_inside_clusters

def main(domaine_entiers, dd_interactions, dm_interactions, conserved_path, SLiMs_list, clusters_orf, cluster_details):
    # Step 1: Eliminate truncated domains from the interactome
    deleted_path = '05_Output/Interactions_dd_domaines_entiers_dans_sORFS/interaction_dd_supprimees.csv'

    processor1 = interactome_sans_domaines_tronqués(domaine_entiers, dd_interactions, conserved_path, deleted_path)
    processor1.process_interactions()

    # Step 2: Create a new interactome using representative ORFs of each cluster
    processor2 = Interactome_cluster_95(clusters_orf, dm_interactions, conserved_path, SLiMs_list)
    processor2.process_files()

    # Step 3: Store the number of interactions made by sORFs within the same cluster
    processor3 = Count_interactions_inside_clusters(conserved_path, dm_interactions, cluster_details)
    processor3.count_interactions()

    print("Analysis completed. Results have been saved in the output files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Elimination of truncated doamins and sORFS that are not representative of a cluster ")
    parser.add_argument("--domaine_entiers", default='01_Reference/domaines_entiers_dans_sORF_ajustement_5aa.csv', help="Path to the list of domains entirely presents in sORFs")
    parser.add_argument("--dd_interactions", default='01_Reference/dd_interactions_monocytes.csv', help="Path to the interactions domain-domain")
    parser.add_argument("--dm_interactions", default='01_Reference/dm_interactions_monocytes_SLiMpval001_ds04over80.csv', help="Path to the interactions domains-motifs")
    parser.add_argument("--conserved_path", default='05_Output/Interactions_dd_domaines_entiers_dans_sORFS/interaction_dd_conservees.csv', help="Output path of the domain-domain interation kept in the analysis")
    parser.add_argument("--SLiMs_list", default='01_Reference/query_slims_SLiMpval001.csv', help="Path to the list of SLiMs detected in sORFs")
    parser.add_argument("--clusters_orf", default='05_Output/Clustering_95/Cluster_orf_monocytes_95', help="Path to the result of the clustering (output of CD-Hit)")
    parser.add_argument("--cluster_details", default='05_Output/Clustering_95/Cluster_orf_monocytes_95.clstr', help="Path to the detailed results of the clustering (output file from CDhit ending with .clstr)")
    args = parser.parse_args()

    main(args.domaine_entiers, args.dd_interactions, args.dm_interactions, args.conserved_path, args.SLiMs_list, args.clusters_orf, args.cluster_details)
