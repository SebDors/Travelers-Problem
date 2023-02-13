import numpy as np
import math as math
from datetime import datetime
from random import sample
from progressbar import ProgressBar, Percentage, Timer, Bar, ETA
import os

# Création d'un tableau contenant les villes et leurs coordonnées géographique
Liste_Des_Villes = [
    ["Paris", 48.8566, 2.3522],
    ["Marseille", 43.2965, 5.3698],
    ["Lyon", 45.764, 4.8357],
    ["Toulouse", 43.6047, 1.4442],
    ["Nice", 43.7101, 7.262],
    ["Nantes", 47.2184, -1.5536]  # ,
    #["Strasbourg", 48.5734, 7.7521],
    #["Montpellier", 43.6107, 3.8767],
    #["Bordeaux", 44.8379, -0.5795],
    #["Lille", 50.6329, 3.0583],
    #["Rennes", 48.1134, -1.6779],
    #["Grenoble", 45.1885, 5.7245],
    #["Rouen", 49.4431, 1.0989],
    #["Saint-Etiennes", 45.4386, 4.3871],
    #["Dijon", 47.3167, 5.0167],
    #["Nimes", 43.8345, 4.3600],
    #["Villeurbannes", 45.7644, 4.8864],
    #["Angers", 47.4784, -0.5602],
    #["Saint-Denis", 48.9358, 2.3596],
    #["Aix-en-Provence", 43.5297, 5.4474],
    #["Brest", 48.3893, -4.486],
    #["Limoges", 45.8319, 1.2621],
    #["Clermont-Ferrand", 45.7833, 3.0833],
    #["Amiens", 49.8941, 2.295],
    #["Nancy", 48.6839, 6.1844],
    #["Roubaix", 50.6942, 3.1746],
    #["Tourcoing", 50.7236, 3.1524],
    #["Orléans", 47.9029, 1.9107],
    #["Mulhouse", 47.7500, 7.3335],
    #["Caen", 49.1828, -0.3715]
]


def LongVille(NomVille):
    """
    Fonction permettant d'acquerir la longitude de la ville dans le tableau
    Entree : NomVille 'string'
    Output : Longitude 'int'    
    """
    for i in range(len(Liste_Des_Villes)):
        if NomVille == Liste_Des_Villes[i][0]:
            return Liste_Des_Villes[i][1]


def LatVille(NomVille):
    """
    Fonction permettant d'acquerir la latitude de la ville dans le tableau
    Entree : NomVille 'string'
    Output : Latitude 'int'    
    """
    for i in range(len(Liste_Des_Villes)):
        if NomVille == Liste_Des_Villes[i][0]:
            return Liste_Des_Villes[i][2]


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
# Valeur maximum que peut comporter un integer
LongueurMin, Emissionmin, Tempsmin = float("inf"), float("inf"), float("inf")
TrajetMin, TrajetTemps, TrajetEmission = "", "", ""
# Clear le terminal
os.system('cls')
# Demander le nombre d'itération à effectuer
NmbIterations = int(input(
    f'Nombre de test ? La probabilitée est de {math.factorial(len(Liste_Des_Villes)-1):_} : '))


def emissionCO2(y):
    if y <= 400:
        emissionsCO2 = 6 * y
    else:
        emissionsCO2 = (6 * 400) + 120 * (y-400)
    return round(emissionsCO2)


def vitessemoyenne(x):
    if x > 200:
        vitessemoyenne = 120
    elif 75 <= x <= 200:
        vitessemoyenne = 80
    else:
        vitessemoyenne = 50
    return vitessemoyenne


def comparaison(Actuel, Min, TrajMin):
    global TrajetActuel
    if Actuel < Min:
        Min = Actuel
        return Actuel, TrajetActuel
    else:
        return Actuel, TrajMin


# Récuperer le temps du début de la simulation
StartTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
# Début de la barre de progression
bar = ProgressBar(widgets=[Percentage(), Timer(),
                           Bar(), ETA()], maxval=NmbIterations)
bar.start()
for i in range(NmbIterations):
    VilleDepart = "Paris"
    emission = 0
    Temps_Trajet_Total = 0
    LongueurActuelle = 0
    TrajetActuel = VilleDepart
    TrajetVilles = sample(
        list(zip(*Liste_Des_Villes))[0][1:], len(list(zip(*Liste_Des_Villes))[0][1:]))
    for j in range(len(TrajetVilles)):
        VilleEtape = TrajetVilles[j]
        LongueurActuelle += Distance_Villes(VilleDepart, VilleEtape)
        emission += emissionCO2(Distance_Villes(VilleDepart, VilleEtape))
        Temps_Trajet_Total += round(Distance_Villes(VilleDepart, VilleEtape) /
                                    vitessemoyenne(Distance_Villes(VilleDepart, VilleEtape)))
        TrajetActuel += " -> " + VilleEtape
        VilleDepart = VilleEtape
    LongueurActuelle += Distance_Villes(VilleDepart, "Paris")
    TrajetActuel += " -> Paris"
    Tempsmin, TrajetTemps = comparaison(
        Tempsmin, Temps_Trajet_Total, TrajetTemps)
    Emissionmin, TrajetEmission = comparaison(
        Emissionmin, emission, TrajetEmission)
    LongueurMin, TrajetMin = comparaison(
        LongueurMin, LongueurActuelle, TrajetMin)
    bar.update(i)

# Calcul du temps mis pour une moyenne de 110km/h
TempsTrajet = round(LongueurMin/110)

# Récuperer le temps final et trouver le delta
EndTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
DeltaTime = EndTime - StartTime
# Convertir en minute si necessaire
if DeltaTime.total_seconds() > 60:
    DeltaTimeMin = DeltaTime.total_seconds()/60
    FinalMessage = f'             Le trajet minimum est : {TrajetMin} \n             Avec une longueur de {round(LongueurMin)} km\r       \n             La durée du voyage à 110 km/h est de {TempsTrajet} heures.\r  \n             Cela a pris {round(DeltaTimeMin)} minutes\r     \n             Les emisions en C02 est de {Emissionmin:_} kgCO2      \n             La durée du voyage est de {Tempsmin} heures\r'
else:
    FinalMessage = f'             Le trajet minimum est : {TrajetMin} \n             Avec une longueur de {round(LongueurMin)} km\r       \n             La durée du voyage à 110 km/h est de {TempsTrajet} heures.\r  \n             Cela a pris {round(DeltaTime.total_seconds())} secondes\r   \n             Les emision en C02 est de {Emissionmin:_} kgCO2      \n             La durée du voyage est de {Tempsmin} heures\r'

if TrajetMin == TrajetEmission:
    FinalMessagee = f'\n             Le trajet minimum est le moins polluant.\r'
else:
    FinalMessagee = f'\n             Le trajet minimum n est pas le moins polluant et c est {TrajetEmission}.\r'

if TrajetMin == TrajetTemps:
    FinalMessagez = f'\n             Le trajet minimum est le plus rapide.\r'
else:
    FinalMessagez = f'\n             Le trajet le plus court n est pas le plus rapide et c est {TrajetTemps}.\r'

# Donner le resultat trajet et km final
print(FinalMessage, FinalMessagee, FinalMessagez)
