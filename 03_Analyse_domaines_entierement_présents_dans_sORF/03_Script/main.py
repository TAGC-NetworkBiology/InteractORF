from Domaines_entiers_dans_sORFs import DomainesProcessor
from Extraction_taille_domaines import Extracteur_taille_domaines_all_PFAM
from sORF_taille_domaines_prédits import sORF_taille_domaines_prédits
from Domaines_entiers_avec_ajustement_5aa import DomainesAlignesAjustésProcessor

def extraire_tailles_domaines_pfam(fichier_hmm):
    """
    Étape 1: Extraction des tailles des domaines présents sur PFAM.
    """
    extracteur_pfam = Extracteur_taille_domaines_all_PFAM(fichier_hmm)
    extracteur_pfam.stocker_taille()
    extracteur_pfam.enregistrer_csv()

def traiter_orfs_et_domaines():
    """
    Étape 2: Calcul de la taille d'alignement des ORFs sur les domaines, si les ORFs ne contiennent pas l'entiéreté du domaine ils sont éliminés .
    """
    fichier_csv_orf_positions = '01_Reference/query_domains.csv'
    fichier_csv_orf_tailles = '05_Output/sORF_taille_domaines_prédits.csv'
    fichier_csv_tailles_pfam = '05_Output/tailles_domaines_all_PFAM.csv'

    orf_processor = sORF_taille_domaines_prédits(fichier_csv_orf_positions)
    orf_processor.calculate_orf_length()
    orf_processor.generate_pfam_length_csv()

    domaines_processor = DomainesProcessor(fichier_csv_orf_tailles, fichier_csv_tailles_pfam)
    domaines_processor.process_domains()

def traiter_domaines_alignes_ajustes():
    """
    Étape 3: Traitement des domaines alignés avec ajustement de 5 aa de chaque côté de l'alignement.
    """
    fichier_csv_orf_tailles = '05_Output/sORF_taille_domaines_prédits.csv'
    fichier_csv_tailles_pfam = '05_Output/tailles_domaines_all_PFAM.csv'
    fichier_csv_orf_positions = '01_Reference/query_domains.csv'

    domaines_alignes_processor = DomainesAlignesAjustésProcessor(fichier_csv_orf_tailles, fichier_csv_tailles_pfam, fichier_csv_orf_positions)
    domaines_alignes_processor.process_domains_alignes_ajustés()

if __name__ == "__main__":
    fichier_hmm = "01_Reference/Pfam-A.hmm"
    
    extraire_tailles_domaines_pfam(fichier_hmm)
    traiter_orfs_et_domaines()
    traiter_domaines_alignes_ajustes()

    print("Scripts exécutés avec succès. Fichiers CSV générés dans le dossier '05_Output'.")
