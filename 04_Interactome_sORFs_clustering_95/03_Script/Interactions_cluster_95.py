import pandas as pd
import re

class Interactome_cluster_95:
    def __init__(self, clusters_orf, dm_interactions, conserved_path, SLiMs_list):
        self.clusters_orf = clusters_orf
        self.dm_interactions = dm_interactions
        self.conserved_path = conserved_path
        self.SLiMs_list = SLiMs_list

    def extract_orf_identifiers(self):
        identifiers = []
        with open(self.clusters_orf, 'r') as orf_file:
            for line in orf_file:
                match = re.match(r'>mORF\|(\w+)\|', line)
                if match:
                    identifiers.append(match.group(1))
        return identifiers

    def extract_csv_identifiers(self, csv_file_path, column_name):
        df = pd.read_csv(csv_file_path, delimiter=',', skipinitialspace=True, low_memory=False)
        identifiers = df[column_name].astype(str).str.strip()
        return identifiers

    def process_files(self):
        orf_identifiers = self.extract_orf_identifiers()
        csv1_column_name = 'Slim_Protein_acc'
        csv1_identifiers = self.extract_csv_identifiers(self.dm_interactions, csv1_column_name)

        csv2_column_name = 'Prot_Accession1'
        csv2_identifiers = self.extract_csv_identifiers(self.conserved_path, csv2_column_name)

        csv3_column_name = 'Seq'
        csv3_identifiers = self.extract_csv_identifiers(self.SLiMs_list, csv3_column_name)

        # Filter and save DataFrames
        dtypes = {'Domain_Description': str, 'supp': str}  # Adjust column names if necessary
        filtered_df1 = pd.read_csv(self.dm_interactions, delimiter=',', dtype=dtypes, skipinitialspace=True, low_memory=False)
        filtered_df1['Domain_Description'] = filtered_df1['Domain_Description'] + ' ' + filtered_df1['supp'].astype(str)
        filtered_df1 = filtered_df1[filtered_df1[csv1_column_name].astype(str).str.strip().isin(orf_identifiers)]
        filtered_df1.to_csv('05_Output/Clustering_95/dm_interactions_monocytes_SLiMpval001_ds04over80_cluster95.csv', index=False)

        filtered_df2 = pd.read_csv(self.conserved_path, delimiter=',', low_memory=False)
        filtered_df2 = filtered_df2[filtered_df2[csv2_column_name].astype(str).str.strip().isin(orf_identifiers)]
        filtered_df2.to_csv('05_Output/Clustering_95/dd_interactions_monocytes_cluster95.csv', index=False)

        filtered_df3 = pd.read_csv(self.SLiMs_list, delimiter=',', low_memory=False)
        filtered_df3 = filtered_df3[filtered_df3[csv3_column_name].astype(str).str.strip().isin(orf_identifiers)]
        filtered_df3.to_csv('05_Output/Clustering_95/interacteurs_slims_monocytes_cluster95.csv', index=False)
        print("Operation completed. Results have been saved in the output files.")

if __name__ == "__main__":
    clusters_orf = '05_Output/Clustering_95/Cluster_orf_monocytes_95'
    dm_interactions = '01_Reference/dm_interactions_monocytes_SLiMpval001_ds04over80.csv'
    conserved_path = '05_Output/Interactions_dd_domaines_entiers_dans_sORFS/interaction_dd_conservees.csv'
    SLiMs_list = '01_Reference/query_slims_SLiMpval001.csv'

    processor = Interactome_cluster_95(clusters_orf, dm_interactions, conserved_path, SLiMs_list)
    processor.process_files()
