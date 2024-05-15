import csv

class interactome_sans_domaines_tronqués:
    def __init__(self, domaine_entiers, dd_interactions, conserved_path, deleted_path):
        self.domaine_entiers = domaine_entiers
        self.dd_interactions = dd_interactions
        self.conserved_path = conserved_path
        self.deleted_path = deleted_path

    def read_identifiers(self, file_path):
        identifiers_signatures = set()
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'orf_id' in row and 'signature' in row:
                    identifiers_signatures.add((row['orf_id'], row['signature']))
        return identifiers_signatures

    def write_csv(self, file_path, rows, fieldnames):
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(rows)

    def process_interactions(self):
        # Read identifiers from the first file
        identifiers_signatures_set = self.read_identifiers(self.domaine_entiers)

        # Read lines from the second file
        rows = []
        fieldnames = []
        with open(self.dd_interactions, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')
            rows = list(reader)
            fieldnames = reader.fieldnames

        # Separate lines based on identifier-signature associations
        conserved_rows = [row for row in rows if (row['Prot_Accession1'], row['Domain_Prot_Accession1']) in identifiers_signatures_set]
        deleted_rows = [row for row in rows if (row['Prot_Accession1'], row['Domain_Prot_Accession1']) not in identifiers_signatures_set]

        # Write results to output files
        self.write_csv(self.conserved_path, conserved_rows, fieldnames)
        self.write_csv(self.deleted_path, deleted_rows, fieldnames)
        print("Operation completed. Results have been saved in the output files.")

if __name__ == "__main__":
    domaine_entiers = '01_Reference/domaines_entiers_dans_sORF_ajustement_5aa.csv'
    dd_interactions = '01_Reference/dd_interactions_monocytes.csv'
    conserved_path = '05_Output/Interactions_dd_domaines_entiers_dans_sORFS/interaction_dd_conservees.csv'
    deleted_path = '05_Output/Interactions_dd_domaines_entiers_dans_sORFS/interaction_dd_supprimees.csv'

    processor = interactome_sans_domaines_tronqués(domaine_entiers, dd_interactions, conserved_path, deleted_path)
    processor.process_interactions()
