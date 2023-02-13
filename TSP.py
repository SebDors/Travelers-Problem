import math as math
import numpy as np

# Définition de la fonction pour obtenir la longitude d'une ville


def LongVille(NomVille, Liste):
    """
    Fonction permettant d'acquerir la longitude de la ville dans le tableau

    Entree : NomVille 'string'
    Output : Longitude 'int'    
    """
    # Boucle pour parcourir toutes les villes dans la liste
    for i in range(len(Liste)):
        # Si le nom de la ville correspond
        if NomVille == Liste[i][0]:
            return Liste[i][1]  # Renvoie la longitude

# Définition de la fonction pour obtenir la latitude d'une ville


def LatVille(NomVille, Liste):
    """
    Fonction permettant d'acquerir la latitude de la ville dans le tableau

    Entree : NomVille 'string'
    Output : Latitude 'int'    
    """
    # Boucle pour parcourir toutes les villes dans la liste
    for i in range(len(Liste)):
        # Si le nom de la ville correspond
        if NomVille == Liste[i][0]:
            return Liste[i][2]  # Renvoie la latitude


# Définition de la fonction pour calculer la distance entre deux villes


def Distance_Villes(VilleA, VilleB):
    """
    Fonction permettant de calculer la distance entre deux villes

    Entree : VilleA,VilleB 'string'
    Return : Distance 'int'
    """
    # Rayon de la Terre en mètre
    Rayon = 6_367_445
    LongA, LongB = math.radians(
        LongVille(VilleA)), math.radians(LongVille(VilleB))
    LatA, LatB = math.radians(LatVille(VilleA)), math.radians(LatVille(VilleB))
    return round((Rayon*(np.arccos(np.sin(LatA)*np.sin(LatB)+np.cos(LatA)*np.cos(LatB)*np.cos(LongB-LongA))))/1000)


def comparaison(ValActuel, ValMin, TrajMin, TrajActuel):
    if ValActuel < ValMin:
        ValMin = ValActuel
        return ValActuel, TrajActuel
    else:
        return ValActuel, TrajMin
