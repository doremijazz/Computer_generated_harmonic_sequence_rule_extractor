import random
from vmo_master.vmo.VMO.oracle import build_oracle, create_oracle

def test_donnees_vraies(input_data, oracle, string_to_numeric, numeric_data):
    """
    Fonction pour tester des données vraies.

    Args:
    - input_data (list): Liste de séquences d'entrée utilisateur.
    - oracle (Oracle): Oracle utilisé pour vérifier les séquences.
    - string_to_numeric (dict): Dictionnaire de correspondance entre les caractères et leurs valeurs numériques.
    - numeric_data (list): Convertisseur en données numériques.

    Returns:
    - tuple: Un tuple contenant un booléen indiquant si toutes les séquences sont acceptées,
             le nombre de tests échoués et le nombre de séquences invalides.
    """

    cpt_check_vrai = 0  # Initialisation du compteur de tests réussis
    test_1_echoue = 0   # Initialisation du compteur de tests échoués
    invalide = 0        # Initialisation du compteur de séquences invalides

    # Effectuer 1000 tests
    for _ in range(1000):
        x = random.randint(0, len(input_data) - 1)
        y = x + 2
        
        # Convertir la séquence en valeurs numériques
        sequence_numeric = [string_to_numeric[string.strip()] for string in input_data[x:y]]

        # Tester si la séquence de l'utilisateur est acceptée
        accepted, final_state = oracle.accept(sequence_numeric)
        
        # Incrémenter les compteurs en conséquence
        if accepted:
            cpt_check_vrai += 1
        else:
            test_1_echoue += 1

    return cpt_check_vrai == 1000, test_1_echoue, invalide

def test_donnees_fausses(input_data, oracle, string_to_numeric, numeric_data):
    """
    Fonction pour tester des données fausses.

    Args:
    - input_data (list): Liste de séquences d'entrée utilisateur.
    - oracle (Oracle): Oracle utilisé pour vérifier les séquences.
    - string_to_numeric (dict): Dictionnaire de correspondance entre les caractères et leurs valeurs numériques.
    - numeric_data (list): Convertisseur en données numériques.

    Returns:
    - tuple: Un tuple contenant un booléen indiquant si toutes les séquences sont rejetées,
             le nombre de tests échoués et le nombre de séquences invalides.
    """

    numeric_to_string = {i: string for string, i in string_to_numeric.items()}
    cpt_check_faux = 0   # Initialisation du compteur de tests réussis
    test_2_echoue = 0    # Initialisation du compteur de tests échoués
    invalide = 0         # Initialisation du compteur de séquences invalides

    # Effectuer 1000 tests
    for _ in range(1000):
        sequence = []
        for _ in range(2):
            # Générer aléatoirement un index valide dans input_data
            index = random.randint(0, len(input_data) - 1)
            sequence.append(input_data[index])
        
        # Convertir la séquence en valeurs numériques
        sequence_numeric = []
        for string in sequence:
            if string.strip() in string_to_numeric:
                sequence_numeric.append(string_to_numeric[string.strip()])
            else:
                invalide += 1

        # Tester si la séquence de l'utilisateur est acceptée
        accepted, final_state = oracle.accept(sequence_numeric)
        
        # Incrémenter les compteurs en conséquence
        if not accepted:
            cpt_check_faux += 1
        else:
            test_2_echoue += 1
    
    return cpt_check_faux == 1000, test_2_echoue, invalide
