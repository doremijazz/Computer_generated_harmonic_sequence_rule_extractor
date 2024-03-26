import pickle
import csv

def sauvegarder_oracle(oracle, string_to_numeric, numeric_data, nom_oracle, nom_dico, nom_convertiseur):
    """
    Fonction pour sauvegarder l'oracle, le dictionnaire de correspondance et le convertisseur numérique.

    Args:
    - oracle: L'objet Oracle à sauvegarder.
    - string_to_numeric (dict): Dictionnaire de correspondance entre les caractères et leurs valeurs numériques.
    - numeric_data (list): Convertiseur en données numériques.
    - nom_oracle (str): Nom du fichier pour sauvegarder l'oracle.
    - nom_dico (str): Nom du fichier pour sauvegarder le dictionnaire de correspondance.
    - nom_convertiseur (str): Nom du fichier pour sauvegarder le convertisseur numérique.
    """

    with open(nom_oracle, 'wb') as fichier:
        pickle.dump(oracle, fichier)  # Sauvegarder l'oracle dans un fichier binaire
    with open(nom_dico, 'wb') as fichier:
        pickle.dump(string_to_numeric, fichier)  # Sauvegarder le dictionnaire de correspondance dans un fichier binaire
    with open(nom_convertiseur, 'wb') as fichier:
        pickle.dump(numeric_data, fichier)  # Sauvegarder le convertisseur numérique dans un fichier binaire

def charger_oracle(nom_fichier, nom_dico, nom_convertiseur):
    """
    Fonction pour charger l'oracle, le dictionnaire de correspondance et le convertisseur numérique depuis les fichiers.

    Args:
    - nom_fichier (str): Nom du fichier contenant l'oracle.
    - nom_dico (str): Nom du fichier contenant le dictionnaire de correspondance.
    - nom_convertiseur (str): Nom du fichier contenant le convertisseur numérique.

    Returns:
    - tuple: Un tuple contenant l'oracle, le dictionnaire de correspondance et le convertisseur numérique.
    """

    with open(nom_fichier, 'rb') as fichier:
        oracle = pickle.load(fichier)  # Charger l'oracle depuis le fichier binaire
    with open(nom_dico, 'rb') as fichier:
        dico = pickle.load(fichier)  # Charger le dictionnaire de correspondance depuis le fichier binaire
    with open(nom_convertiseur, 'rb') as fichier:
        convertisseur = pickle.load(fichier)  # Charger le convertisseur numérique depuis le fichier binaire
    
    return oracle, dico, convertisseur

