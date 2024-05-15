import pandas as pd

class DomainesAlignesAjustésProcessor:
    def __init__(self, orf_domaines_file, tailles_domaines_pfam_file, orf_positions_file):
        self.orf_domaines_df = pd.read_csv(orf_domaines_file, sep=',')
        self.tailles_domaines_pfam_df = pd.read_csv(tailles_domaines_pfam_file, sep=',')
        self.orf_positions_df = pd.read_csv(orf_positions_file, sep='\t')
        self.merged_df = None

    def process_domains_alignes_ajustés(self):
        self.tailles_domaines_pfam_df['ACC'] = self.tailles_domaines_pfam_df['ACC'].str.split('.').str[0]

        self.merged_df = pd.merge(self.orf_domaines_df, self.tailles_domaines_pfam_df,
                                  left_on='signature', right_on='ACC', how='left')

        self.merged_df = self.merged_df.drop(columns=['ACC'])
        self.merged_df = self.merged_df.rename(columns={'Taille': 'Taille_réelle_domaine'})
        print(self.merged_df.columns)

        # Ajouter les positions de début et de fin depuis le fichier d'origine
        self.merged_df = pd.merge(self.merged_df, self.orf_positions_df[['orf_id', 'start_pos', 'end_pos']],
                                  on='orf_id', how='left')

        # Recalculer la taille en fonction des nouvelles positions
        self.merged_df['adjusted_start_pos'] = self.merged_df['start_pos'] - 5
        self.merged_df.loc[self.merged_df['adjusted_start_pos'] < 1, 'adjusted_start_pos'] = 1
        self.merged_df['adjusted_end_pos'] = self.merged_df['end_pos'] + 5

        # Calculer la différence entre adjusted_end_pos et adjusted_start_pos
        self.merged_df['difference_taille_ajustée'] = self.merged_df['adjusted_end_pos'] - self.merged_df['adjusted_start_pos']

        # Filtrer les domaines alignés entiers en fonction de la différence calculée
        aligned_domains_entiers_df = self.merged_df[
            self.merged_df['difference_taille_ajustée'] >= self.merged_df['Taille_réelle_domaine']
        ]

        # Filtrer les domaines alignés tronqués en fonction de la différence calculée
        aligned_domains_eliminés_df = self.merged_df[
            ~(self.merged_df['difference_taille_ajustée'] >= self.merged_df['Taille_réelle_domaine'])
        ]

        # Enregistrer les domaines alignés entiers dans un fichier CSV
        aligned_domains_entiers_df.to_csv('05_Output/domaines_entiers_dans_sORF_ajustement_5aa.csv', index=False)

        # Enregistrer les domaines alignés tronqués dans un fichier CSV
        aligned_domains_eliminés_df.to_csv('05_Output/domaines_eliminés_ap_ajustement_5aa.csv', index=False)

if __name__ == "__main__":
    orf_domaines_file_path = '05_Output/sORF_taille_domaines_prédits.csv'
    tailles_domaines_pfam_file_path = '05_Output/tailles_domaines_all_PFAM.csv'
    orf_positions_file_path = '01_Reference/spep_domains_mediating_int_df.csv'

    aligned_domains_processor = DomainesAlignesAjustésProcessor(orf_domaines_file_path, tailles_domaines_pfam_file_path, orf_positions_file_path)
    aligned_domains_processor.process_domains_alignes_ajustés()
