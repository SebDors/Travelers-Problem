import numpy as np
import math as math
from datetime import datetime
from random import sample
from progressbar import ProgressBar, Percentage, Timer, Bar, ETA
import os

# Création d'un tableau contenant les villes et leurs coordonnées géographique
Liste_Des_Villes = [["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier"],
                    [48.8566, 43.2965, 45.764, 43.6047,
                        43.7101, 47.2184, 48.5734, 43.62505],
                    [2.3522, 5.3698, 4.8357, 1.4442, 7.262, -1.5536, 7.7521, 3.862038]]


def LongVille(NomVille):
    """
    Fonction permettant d'acquerir la longitude de la ville dans le tableau

    Entree : NomVille 'string'
    Output : Longitude 'int'    
    """
    for i in range(len(Liste_Des_Villes[0])):
        if NomVille == Liste_Des_Villes[0][i]:
            return Liste_Des_Villes[1][i]


def LatVille(NomVille):
    """
    Fonction permettant d'acquerir la latitude de la ville dans le tableau

    Entree : NomVille 'string'
    Output : Latitude 'int'    
    """
    for i in range(len(Liste_Des_Villes[0])):
        if NomVille == Liste_Des_Villes[0][i]:
            return Liste_Des_Villes[2][i]


def Distance_Villes(VilleA, VilleB):
    """
    Fonction permettant de calculer la distance entre deux villes

    Entree : VilleA,VilleB 'string'
    Return : Distance 'int'
    """
    Rayon = 6_367_445
    LongA, LongB = math.radians(
        LongVille(VilleA)), math.radians(LongVille(VilleB))
    LatA, LatB = math.radians(LatVille(VilleA)), math.radians(LatVille(VilleB))
    return round((Rayon*(np.arccos(np.sin(LatA)*np.sin(LatB)+np.cos(LatA)*np.cos(LatB)*np.cos(LongB-LongA))))/1000)


# Initialisation des variables générales
LongueurMin = float("inf")  # Valeure maximum que peut comporter un integer
TrajetMin = ""
# Clear le terminal
os.system('cls')
# Demander le nombre d'itération à effectuer
NmbIterations = int(input(
    f'Nombre de test ? La probabilitée est de {math.factorial(len(Liste_Des_Villes [0]))} : '))


def ComparaisonDistance(x):
    """
    Comparer la la distance entre le trajet en cours et le trajet minimal

    Entree : x 'int'
    return : None
    """
    global LongueurMin
    global TrajetMin
    if LongueurMin > x:
        LongueurMin = x
        TrajetMin = TrajetActuel


# Récuperer le temps du début de la simulation
StartTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
# Début de la barre de progression
bar = ProgressBar(widgets=[Percentage(), Timer(),
                           Bar(), ETA()], maxval=NmbIterations)
bar.start()
for i in range(NmbIterations):

    LongueurActuelle = 0
    VilleDepart = "Paris"
    TrajetActuel = VilleDepart
    TrajetVilles = sample(
        Liste_Des_Villes[0][1:], len(Liste_Des_Villes[0][1:]))
    for j in range(len(TrajetVilles)):
        VilleEtape = TrajetVilles[j]
        LongueurActuelle += Distance_Villes(VilleDepart, VilleEtape)
        TrajetActuel += " -> " + VilleEtape
        VilleDepart = VilleEtape
    LongueurActuelle += Distance_Villes(VilleDepart, "Paris")
    TrajetActuel += " -> Paris"
    ComparaisonDistance(LongueurActuelle)
    bar.update(i)

# Récuperer le temps final et trouver le delta
EndTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
DeltaTime = EndTime - StartTime
# Convertir en minute si necessaire
if DeltaTime.total_seconds() > 60:
    DeltaTimeMin = DeltaTime.total_seconds()/60
    FinalMessage = f'Le trajet minimum est : {TrajetMin} avec {round(LongueurMin)} km.\r\nCela a pris {DeltaTimeMin} minutes'
else:
    FinalMessage = f'Le trajet minimum est : {TrajetMin} avec {round(LongueurMin)} km.\r\nCela a pris {DeltaTime.total_seconds()} secondes'

# Donner le resultat trajet et km final
print(FinalMessage)
