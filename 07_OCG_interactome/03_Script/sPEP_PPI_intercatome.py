import csv

class Merge_sPEP_PPI_interactome:
    def __init__(self, interaction_domain_domain, interaction_domain_motif, sPEP_interactome, Canonical_protein_interactome, merged_interactome):
        self.interaction_domain_domain = interaction_domain_domain
        self.interaction_domain_motif = interaction_domain_motif
        self.sPEP_interactome = sPEP_interactome
        self.Canonical_protein_interactome = Canonical_protein_interactome
        self.merged_interactome = merged_interactome

    def read_csv(self, file_path):
        data = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def write_txt(self, file_path, data):
        with open(file_path, 'w') as file:
            for entry in data:
                file.write(f"{entry[0]}\t{entry[1]}\n")

    def generate_associations(self):
        data1 = self.read_csv(self.interaction_domain_domain)
        data2 = self.read_csv(self.interaction_domain_motif)

        associations = set()

        for row in data2:
            association = (row['Slim_Protein_acc'], row['Prot_Accession'])
            associations.add(association)

        for row in data1:
            association = (row['Prot_Accession1'], row['Prot_Accession2'])
            associations.add(association)

        self.write_txt(self.sPEP_interactome, associations)

        with open(self.sPEP_interactome, 'r') as file:
            content = file.readlines()

        with open(self.Canonical_protein_interactome, 'r') as file:
            additional_content = file.readlines()

        with open(self.merged_interactome, 'w') as file:
            file.writelines(content)
            file.writelines(additional_content)


if __name__ == "__main__":
    interaction_domain_domain = "01_Reference/dd_interactions_monocytes_cluster95.csv"
    interaction_domain_motif = "01_Reference/dm_interactions_monocytes_SLiMpval001_ds04over80_cluster95.csv"
    sPEP_interactome = "05_Output/SPEP_interactome_monocytes.txt"
    Canonical_protein_interactome = "01_Reference/PPI_MoonDB_UniProtAcc_monocytes.ncol"
    merged_interactome = "05_Output/SPEPPI_PPI_interactome_monocytes.txt"

    merger = Merge_sPEP_PPI_interactome(interaction_domain_domain, interaction_domain_motif, sPEP_interactome, Canonical_protein_interactome, merged_interactome)
    merger.generate_associations()
