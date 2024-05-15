import os
import pandas as pd

class Extracteur_taille_domaines_all_PFAM:
    def __init__(self, chemin_fichier):
        """
        Initialise l'extracteur de tailles de domaines PFAM.

        Parameters:
        - chemin_fichier (str): Le chemin vers le fichier contenant les informations des domaines PFAM.
        """
        self.chemin_fichier = chemin_fichier
        self.tailles_domaines = []

    def extraire_infos_domaine(self, lines):
        """
        Extrait l'identifiant (ACC) et la taille d'un domaine PFAM à partir des lignes fournies.

        Parameters:
        - lines (list): La liste des lignes représentant les informations d'un domaine PFAM.

        Returns:
        - tuple or None: Un tuple contenant l'identifiant (ACC) et la taille du domaine, ou None si l'information n'est pas trouvée.
        """
        acc = None
        taille = None

        for line in lines:
            if line.startswith("ACC"):
                acc = line.split()[1]
            elif line.startswith("LENG"):
                taille = line.split()[1]

        if acc and taille:
            return acc, taille
        else:
            return None

    def stocker_taille(self):
        """
        Parcourt le fichier, extrait les identifiants et les tailles des domaines PFAM, et les stocke dans la liste des tailles.
        """
        # Liste temporaire pour stocker les lignes d'un domaine
        lignes_domaine = []

        # Lire le fichier ligne par ligne
        with open(self.chemin_fichier, "r") as fichier:
            lignes = fichier.readlines()

            for ligne in lignes:
                # Vérifier si c'est une ligne vide ou une ligne contenant "//"
                if ligne.strip() == "//":
                    # Extraire l'identifiant et la taille du domaine et réinitialiser la liste temporaire
                    infos_domaine = self.extraire_infos_domaine(lignes_domaine)
                    if infos_domaine:
                        acc, taille = infos_domaine
                        self.tailles_domaines.append({"ACC": acc, "Taille": taille})
                    lignes_domaine = []
                else:
                    # Ajouter la ligne à la liste temporaire
                    lignes_domaine.append(ligne)

    def enregistrer_csv(self, dossier_output="05_Output", nom_fichier_csv="tailles_domaines_all_PFAM.csv"):
        """
        Enregistre les identifiants et les tailles des domaines PFAM dans un fichier CSV.

        Parameters:
        - dossier_output (str): Le dossier dans lequel enregistrer le fichier CSV.
        - nom_fichier_csv (str): Le nom du fichier CSV.
        """
        # Créer un DataFrame à partir des identifiants et des tailles extraites
        df = pd.DataFrame(self.tailles_domaines)

        # Vérifier si le dossier existe, sinon le créer
        if not os.path.exists(dossier_output):
            os.makedirs(dossier_output)

        # Enregistrer le DataFrame au format CSV dans le dossier spécifié
        chemin_fichier_csv = os.path.join(dossier_output, nom_fichier_csv)
        df.to_csv(chemin_fichier_csv, index=False)

        print(f"Les identifiants et les tailles ont été enregistrés dans {chemin_fichier_csv}.")

# Exemple d'utilisation dans un autre script
if __name__ == "__main__":
    chemin_fichier = "01_Reference/Pfam-A.hmm"
    extracteur = Extracteur_taille_domaines_all_PFAM(chemin_fichier)
    extracteur.stocker_taille()
    extracteur.enregistrer_csv()
