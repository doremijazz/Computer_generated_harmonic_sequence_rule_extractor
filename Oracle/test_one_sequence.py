from vmo_master.vmo.VMO.oracle import build_oracle, create_oracle  # Importer les fonctions d'oracle

def test_sequence(sequence, oracle, string_to_numeric):
    """
    Fonction pour tester une séquence donnée avec l'oracle.

    Args:
    - sequence (list): Séquence à tester.
    - oracle: L'objet Oracle utilisé pour effectuer le test.
    - string_to_numeric (dict): Dictionnaire de correspondance entre les caractères et leurs valeurs numériques.

    Returns:
    - bool: True si la séquence est acceptée, False sinon.
    """

    # Convertir la séquence en valeurs numériques
    sequence_numeric = []
    for accord in sequence:
        print(accord)  # Afficher chaque accord (utile pour le débogage)
        
        # Vérifier si la clé existe dans le dictionnaire
        if accord in string_to_numeric:
            # Ajouter la valeur numérique correspondante à la séquence
            sequence_numeric.append(string_to_numeric[accord])
        else:
            # Gérer le cas où la clé n'existe pas dans le dictionnaire
            print("La clé '{}' n'existe pas dans le dictionnaire.".format(accord))
            # Vous pouvez choisir de gérer cette situation selon vos besoins

    # Testez si la séquence de l'utilisateur est acceptée
    accepted, final_state = oracle.accept(sequence_numeric)

    return accepted

