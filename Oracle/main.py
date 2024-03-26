import sys
import time
from tqdm import tqdm  # Importation de tqdm pour la barre de progression
from build_oracle import oracle_func
from create_input_data import recuperer_tableau, Liste_elements_tableau_2d
from save_or_load_oracle import sauvegarder_oracle, charger_oracle
from test_one_sequence import test_sequence
from test_validation import test_donnees_vraies, test_donnees_fausses

def main(exercice, iteration):
    """
    Fonction principale pour exécuter le processus principal.

    Args:
    - exercice (str): Tableau contenant la séquence que l'utilisateur
    souhaite vérifier. Elle est vide si l'utilisateur souhaite effectuer
    la validation de l'oracle.

    Returns:
    - bool: Résultat de la vérification de l'exercice ou de la validation.
    """

    # Noms des fichiers pour l'oracle, le dictionnaire et le convertisseur
    nom_fichier_oracle = "oracle_bach.pkl"
    nom_dico = "dico_bach.pkl"
    nom_convertiseur = "convertiseur.pkl"

    # Récupération des données d'entrée et initialisation de la liste d'éléments
    input_data = recuperer_tableau()
    liste_elements = Liste_elements_tableau_2d(input_data)

    try:
        # Chargement de l'oracle, du dictionnaire et du convertisseur depuis les fichiers
        oracle_charge, dico_charge, convertiseur_charge = charger_oracle(nom_fichier_oracle, nom_dico, nom_convertiseur)
        print("\nOracle chargé depuis le fichier.")

    except FileNotFoundError:
        print("\nLe fichier de l'oracle n'existe pas. Création d'un nouvel oracle...")

        # Création d'un nouvel oracle, d'un dictionnaire et d'un convertisseur
        oracle, string_to_numeric, numeric_data = oracle_func(liste_elements)
        
        # Sauvegarde de l'oracle dans un fichier
        sauvegarder_oracle(oracle, string_to_numeric, numeric_data, nom_fichier_oracle, nom_dico, nom_convertiseur)
        print("\nOracle sauvegardé dans le fichier.")
        
        # Rechargement de l'oracle, du dictionnaire et du convertisseur depuis les fichiers
        oracle_charge, dico_charge, convertiseur_charge = charger_oracle(nom_fichier_oracle, nom_dico, nom_convertiseur)

    # Impression du dictionnaire de correspondance (utile pour le débogage)
    ##print(dico_charge)
    
    # Mesure du temps d'exécution
    start_time = time.time()
    
    # Appel de la fonction pour vérifier l'exercice ou la validation
    result = verifier_exercice_ou_validation(exercice, liste_elements, oracle_charge, dico_charge, convertiseur_charge, iteration)


    # Afficher le résultat final
    print("\nRésulatat du test",result)
    

def verifier_exercice_ou_validation(exercice, input_data, oracle_charge, dico_charge, convertiseur_charge, iteration):
    if len(exercice) < 1:
        # Initialisation d'une liste pour stocker les pourcentages d'échecs
        pourcentages_echecs = []

        # Test des données vraies et fausses avec barre de progression
        for i in tqdm(range(iteration), desc="Tests en cours", ncols=75, mininterval=3, smoothing=0.5):
            test_vraies, test_1_echoue, invalide = test_donnees_vraies(input_data, oracle_charge, dico_charge, convertiseur_charge)
            test_fausses, test_2_echoue, invalide = test_donnees_fausses(input_data, oracle_charge, dico_charge, convertiseur_charge)

            if not test_fausses:
                # Ajout du pourcentage d'échec du test 2 à la liste
                pourcentage_2_faux = (test_2_echoue / 1000) * 100
                pourcentages_echecs.append(pourcentage_2_faux)

        # Calcul de la moyenne des pourcentages d'échecs
        if len(pourcentages_echecs) > 0:
            moyenne_echecs = "{:.2f}%".format(sum(pourcentages_echecs) / len(pourcentages_echecs))
        else:
            moyenne_echecs = 0  # Ou une autre valeur par défaut

        # Retour des résultats
        return test_vraies, test_fausses, moyenne_echecs
    else:
        # Test de la séquence fournie par l'utilisateur
        test_result = test_sequence(exercice, oracle_charge, dico_charge)
        
        # Retour du résultat de la vérification de l'exercice
        return test_result

# Vérification de l'existence des arguments
if len(sys.argv) == 1:
    print("\nAucun argument n'a été fourni.")
    exercice = []

    ############# On peut changer le nombre d'iteration ICI #################
    iteration = 100
else:
    print("\nDes arguments ont été fournis.")
    exercice = sys.argv[0]
    iteration = 0

if __name__ == "__main__":
    # Appel de la fonction principale avec mesure du temps d'exécution
    start_time = time.time()
    resultat = main(exercice, iteration)
    elapsed_time = time.time() - start_time
    
    # Affichage du temps d'exécution total
    print(f"\nTemps d'exécution total : {elapsed_time} secondes")
    #print(resultat)
