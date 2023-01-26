import numpy as np
import math as math

Liste_Des_Villes = [["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
                    [48.8566, 43.2965, 45.764, 43.6047, 43.7101],
                    [2.3522, 5.3698, 4.8357, 1.4442, 7.262],
                    [0,       0,     0,     0,       0]]


def InfoVille(NomVille):
    for i in range(len(Liste_Des_Villes[0])):
        if NomVille == Liste_Des_Villes[0][i]:
            print(Liste_Des_Villes[1][i], Liste_Des_Villes[2]
                  [i], Liste_Des_Villes[3][i])


def LongVille(NomVille):
    for i in range(len(Liste_Des_Villes[0])):
        if NomVille == Liste_Des_Villes[0][i]:
            return Liste_Des_Villes[1][i]


def LatVille(NomVille):
    for i in range(len(Liste_Des_Villes[0])):
        if NomVille == Liste_Des_Villes[0][i]:
            return Liste_Des_Villes[2][i]


def Distance_Villes(VilleA, VilleB):
    Rayon = 6_367_445
    LongA, LongB = LongVille(VilleA), LongVille(VilleB)
    LatA, LatB = LatVille(VilleA), LatVille(VilleB)
    LongA, LongB = math.radians(LongA), math.radians(LongB)
    LatA, LatB = math.radians(LatA), math.radians(LatB)
    return Rayon*(np.arccos(np.sin(LatA)*np.sin(LatB)+np.cos(LatA)*np.cos(LatB)*np.cos(LongB-LongA)))


LongueurMin = 0
TrajetMin = ""
#NmbIterations = int(input("Number of iterations ?"))
VilleDépart = "Paris"

"""for i in range(NmbIterations):"""
while Liste_Des_Villes[3][0] == 0:
    # Choix de la prochaine destination
    ChoixDeVille = np.random.randint(1, (len(Liste_Des_Villes[0])))
    print(Liste_Des_Villes[3][ChoixDeVille])

    while Liste_Des_Villes[3][ChoixDeVille] == 1:
        # Check si nous n'avons pas pris une destination déjà prise
        ChoixDeVille = np.random.randint(1, (len(Liste_Des_Villes[0])))
    VilleEtape = Liste_Des_Villes[0][ChoixDeVille]

    # Ajouter un 1 pour prevenir que nous sommes déjà passé par cette destination
    Liste_Des_Villes[3][ChoixDeVille] = 1
    # Donner la destination avec le kilometrage
    print(VilleDépart, "-> ", VilleEtape, " = ", Distance_Villes(VilleDépart, VilleEtape)/1000, "km")

    # Intervertir Ville de départ et ville d'arrivée*
    VilleDépart = VilleEtape

    # Checker si nous n'avons pas fais toutes les destinations
