class Count_binary_interactions:
    def __init__(self, interaction_file_path):
        self.interaction_file_path = interaction_file_path

    def count_unique_interactions(self):
        with open(self.interaction_file_path, "r") as f:
            next(f)
            interactions_uniques = set()
            for line in f:
                columns = line.strip().split(",")
                if len(columns) < 6:
                    continue
                accession1 = columns[0]
                accession2 = columns[5]
                if (accession1, accession2) not in interactions_uniques and (accession2, accession1) not in interactions_uniques:
                    interactions_uniques.add((accession1, accession2))
        return len(interactions_uniques)

if __name__ == "__main__":
    interaction_file_path = "05_Output/Clustering_95/dd_interactions_monocytes_cluster95.csv"
    processor = Count_binary_interactions(interaction_file_path)
    unique_interactions_count = processor.count_unique_interactions()
    print("Le nombre d'interactions binaires uniques est:", unique_interactions_count)
