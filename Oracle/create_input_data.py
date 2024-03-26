import pickle

def recuperer_tableau():
    """
    Fonction pour récupérer un tableau contenant les chorals analyses à partir d'un fichier pickle.

    Returns:
    - list: Le tableau récupéré.
    """
    # Nom du fichier depuis lequel on récupère le tableau
    nom_fichier = "tableau.pkl"

    # Ouvrir le fichier en mode lecture binaire (rb) pour la récupération
    with open(nom_fichier, 'rb') as fichier:
        tableau_recupere = pickle.load(fichier)

    return tableau_recupere

def Liste_elements_tableau_2d(tableau_2d):
    """
    Fonction pour créer une liste en fusionnant les notes de la mélodie et les accords.

    Args:
    - tableau_2d (list): Tableau 2D contenant des éléments.

    Returns:
    - list: Liste fusionnée d'éléments.
    """
    liste = []
    L_chords = []
    L_melodie = []
    
    # Parcourir les lignes du tableau 2D
    for index, ligne in enumerate(tableau_2d):
        if index % 2 == 1:
            # Si l'indice de ligne est impair, ajouter les éléments à la liste des accords
            for element in ligne:
                L_chords.append(element)
        else:
            # Si l'indice de ligne est pair, ajouter les éléments à la liste de mélodie
            for element in ligne:
                L_melodie.append(element)
    
    # Fusionner les éléments de mélodie et d'accord de manière spécifique pour créer la liste finale
    for i in range(len(L_chords)):
        if i > 0:
            liste.append(L_chords[i - 1] + str(L_melodie[i]))
                
    return liste

