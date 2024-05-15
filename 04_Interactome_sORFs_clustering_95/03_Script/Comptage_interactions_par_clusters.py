import re
import pandas as pd

class Count_interactions_inside_clusters:
    def __init__(self, conserved_path, dm_interactions, cluster_details):
        self.conserved_path = conserved_path
        self.dm_interactions = dm_interactions
        self.cluster_details = cluster_details
        self.clusters_dict = {}

    def extract_orf_identifiers(self, line):
        return re.findall(r'>mORF\|(\w+)', line)

    def load_clusters(self):
        with open(self.cluster_details, 'r') as cluster:
            current_cluster = None

            for line in cluster:
                if line.startswith(">Cluster"):
                    current_cluster = line.strip()
                    self.clusters_dict[current_cluster] = []
                elif current_cluster is not None:
                    orfs = self.extract_orf_identifiers(line)
                    self.clusters_dict[current_cluster].extend(orfs)

    def count_interactions(self):
        self.load_clusters()

        # Load interaction files as DataFrames
        df_dd = pd.read_csv(self.conserved_path, delimiter=',')
        df_dm = pd.read_csv(self.dm_interactions, delimiter=',', low_memory=False)

        # DataFrames cleanup
        df_dd_cleaned = df_dd[['Prot_Accession1', 'Prot_Accession2']].drop_duplicates()
        df_dm_cleaned = df_dm[['Slim_Protein_acc', 'Prot_Accession']].drop_duplicates()

        comptage_interactions_dd = {'Protéine': [], 'Cluster': [], 'Comptage_Interactions_dd': []}
        comptage_interactions_dm = {'Protéine': [], 'Cluster': [], 'Comptage_Interactions_dm': []}

        for cluster in self.clusters_dict.keys():
            interactions_dd = []
            interactions_dm = []

            for orf in self.clusters_dict[cluster]:
                dd_interactions = df_dd_cleaned[df_dd_cleaned['Prot_Accession1'] == orf]
                dm_interactions = df_dm_cleaned[df_dm_cleaned['Slim_Protein_acc'] == orf]

                interactions_dd.extend(list(dd_interactions['Prot_Accession2']))
                interactions_dm.extend(list(dm_interactions['Prot_Accession']))

            comptage_dd = pd.Series(interactions_dd).value_counts().reset_index()
            comptage_dd.columns = ['Protéine', 'Comptage_Interactions_dd']

            comptage_dm = pd.Series(interactions_dm).value_counts().reset_index()
            comptage_dm.columns = ['Protéine', 'Comptage_Interactions_dm']

            for idx, row in comptage_dd.iterrows():
                comptage_interactions_dd['Protéine'].append(row['Protéine'])
                comptage_interactions_dd['Cluster'].append(cluster)
                comptage_interactions_dd['Comptage_Interactions_dd'].append(row['Comptage_Interactions_dd'])

            for idx, row in comptage_dm.iterrows():
                comptage_interactions_dm['Protéine'].append(row['Protéine'])
                comptage_interactions_dm['Cluster'].append(cluster)
                comptage_interactions_dm['Comptage_Interactions_dm'].append(row['Comptage_Interactions_dm'])

        df_comptage_dd = pd.DataFrame(comptage_interactions_dd)
        df_comptage_dm = pd.DataFrame(comptage_interactions_dm)

        df_comptage_dd['Cluster'] = df_comptage_dd['Cluster'].str.extract('(\d+)').astype(float)
        df_comptage_dm['Cluster'] = df_comptage_dm['Cluster'].str.extract('(\d+)').astype(float)

        df_comptage_dd = df_comptage_dd[['Cluster', 'Protéine', 'Comptage_Interactions_dd']]
        df_comptage_dm = df_comptage_dm[['Cluster', 'Protéine', 'Comptage_Interactions_dm']]

        df_comptage_dd = df_comptage_dd.sort_values(['Cluster', 'Protéine'])
        df_comptage_dm = df_comptage_dm.sort_values(['Cluster', 'Protéine'])

        df_comptage_dd.to_csv("05_Output/Comptages_interactions_par_clusters/comptage_interactions_dd_par_prot.csv", index=False)
        df_comptage_dm.to_csv("05_Output/Comptages_interactions_par_clusters/comptage_interactions_dm_par_prot.csv", index=False)

if __name__ == "__main__":
    conserved_path = "05_Output/Interactions_dd_domaines_entiers_dans_sORFS/interaction_dd_conservees.csv"
    dm_interactions = "01_Reference/dm_interactions_monocytes_SLiMpval001_ds04over80.csv"
    cluster_details = "05_Output/Clustering_95/Cluster_orf_monocytes_95.clstr"

    processor = Count_interactions_inside_clusters(conserved_path, dm_interactions, cluster_details)
    processor.count_interactions()
