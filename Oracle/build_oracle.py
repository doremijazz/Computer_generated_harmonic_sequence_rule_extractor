import pickle
import csv
import random
import sys
from vmo_master.vmo.VMO.oracle import build_oracle, create_oracle


def oracle_func(input_data):
    """
    Fonction pour créer un oracle à partir des données d'entrée.

    Args:
    - input_data (list): Liste de chaînes de caractères en entrée. Sous la forme "C60" avec l'accord
    la note de la melodie en valeur MIDI.

    Returns:
    - tuple: Un tuple contenant l'oracle, le dictionnaire de correspondance et le convertiseur en données numériques.
    """

    # Créer un dictionnaire pour mapper chaque chaîne unique à une valeur numérique
    string_to_numeric = {string: i for i, string in enumerate(set(input_data))}
    
    # Convertir vos données de chaînes de caractères à des valeurs numériques
    numeric_data = [string_to_numeric[string] for string in input_data]

    # Réglez le seuil en fonction de vos besoins
    threshold = 0.5

    # Créer un oracle de type 'f' (Factor Oracle)
    oracle = create_oracle('f', threshold=threshold)

    # Construire l'oracle avec les données numériques
    oracle = build_oracle(numeric_data, flag='f', threshold=threshold)

    # Retourner l'oracle, le dictionnaire de correspondance et les données numériques
    return oracle, string_to_numeric, numeric_data

