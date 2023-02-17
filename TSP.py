import math as math
import numpy as np


def LatVille(NomVille, Liste):
    """
    Fonction permettant d'acquerir la latitude de la ville dans un tableau

    Entree : NomVille 'string'
    Output : Longitude 'int'    

    La liste doit être de ce format: [Nom de la ville, Latitude, Longitude]
    """
    # Boucle pour parcourir toutes les villes dans la liste
    for i in range(len(Liste)):
        # Si le nom de la ville correspond
        if NomVille == Liste[i][0]:
            return Liste[i][1]  # Renvoie la longitude


def LongVille(NomVille, Liste):
    """
    Fonction permettant d'acquerir la longitude de la ville dans un tableau

    Entree : NomVille 'string'
    Output : Latitude 'int'    
    La liste doit être de ce format: [Nom de la ville, Latitude, Longitude]
    """
    # Boucle pour parcourir toutes les villes dans la liste
    for i in range(len(Liste)):
        # Si le nom de la ville correspond
        if NomVille == Liste[i][0]:
            return Liste[i][2]  # Renvoie la latitude


def Distance_Villes(VilleA, VilleB, Liste):
    """
    Fonction permettant de calculer la distance entre deux villes dans un tableau 

    Entree : VilleA,VilleB 'string'
    Return : Distance 'int'
    """
    # Rayon de la Terre en mètre
    Rayon = 6_367_445
    LongA, LongB = math.radians(
        LongVille(VilleA, Liste)), math.radians(LongVille(VilleB, Liste))
    LatA, LatB = math.radians(LatVille(VilleA, Liste)
                              ), math.radians(LatVille(VilleB, Liste))
    return round((Rayon*(np.arccos(np.sin(LatA)*np.sin(LatB)+np.cos(LatA)*np.cos(LatB)*np.cos(LongB-LongA))))/1000)


def comparaison(ValActuel, ValMin, TrajMin, TrajActuel):
    """
    Fonction permettant de faire une comparaison entre 2 valeurs.
    Si la valeur actuelle ValActuel < ValMin, alors elle renvoie les valeurs actuels a prendre.
    Sinon elle reste sur les valeurs antérieurs

    Input : ValActuel, ValMin, TrajMin, TrajActuel 'int'
    Output : ValActuel, (TrajActuel OR TrajMin)

    exemple : ValActuel = 200km
              ValMin = 260km
              TrajMin = Paris -> Marseille -> Montpellier
              TrajActuel = Paris -> Montpellier -> Marseille
    ValActuel < ValMin donc ValMin et TrajMin vaudront '200km' et 'Paris -> Montpellier -> Marseille'
    """
    if ValActuel < ValMin:
        return ValActuel, TrajActuel
    else:
        return ValMin, TrajMin
