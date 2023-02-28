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
    ["Nantes", 47.2184, -1.5536],
    ["Strasbourg", 48.5734, 7.7521],
    ["Montpellier", 43.6107, 3.8767],
    ["Bordeaux", 44.8379, -0.5795],
    ["Lille", 50.6329, 3.0583],
    ["Rennes", 48.1134, -1.6779],
    ["Grenoble", 45.1885, 5.7245],
    ["Rouen", 49.4431, 1.0989],
    ["Saint-Etiennes", 45.4386, 4.3871],
    ["Dijon", 47.3167, 5.0167],
    ["Nimes", 43.8345, 4.3600],
    ["Villeurbannes", 45.7644, 4.8864],
    ["Angers", 47.4784, -0.5602],
    ["Saint-Denis", 48.9358, 2.3596],
    ["Aix-en-Provence", 43.5297, 5.4474],
    ["Brest", 48.3893, -4.486],
    ["Limoges", 45.8319, 1.2621],
    ["Clermont-Ferrand", 45.7833, 3.0833],
    ["Amiens", 49.8941, 2.295],
    ["Nancy", 48.6839, 6.1844],
    ["Roubaix", 50.6942, 3.1746],
    ["Tourcoing", 50.7236, 3.1524],
    ["Orléans", 47.9029, 1.9107],
    ["Mulhouse", 47.7500, 7.3335],
    ["Caen", 49.1828, -0.3715]
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


def EmissionCO2Calcul(km):
    """
    Fonction calculant l'emission de CO2 de la voiture pour chaques trajet entre les villes
    Electrique 6g/km Autonimie 400km
    Thermique 120g/km Autonomie infinie

    Input : km 'int'
    Output : None
    """
    global EmissionCO2Actuel
    if km <= 400:
        return 6*km
    else:
        return (6*400 + (km-400)*120)


def ComparaisonDistance(x):
    """
    Comparer la distance entre le trajet en cours et le trajet minimal

    Input : x 'int'
    Output : None
    """
    global LongueurMin
    global TrajetMin
    if LongueurMin > x:
        LongueurMin = x
        TrajetMin = TrajetActuel


def ComparaisonEmission(x):
    """
    Comparer l'émission en C02 entre le trajet en cours et le trajet minimal

    Input : x 'int'
    Output : None
    """
    global EmissionCO2Min
    global TrajetEmissionC02
    if EmissionCO2Min > x:
        EmissionCO2Min = x
        TrajetEmissionC02 = TrajetActuel


# Initialisation des variables générales
LongueurMin = float("inf")  # Valeure maximum que peut comporter un integer
EmissionCO2Min = float("inf")
TrajetMin = ""
TrajetEmissionC02 = ""
# Clear le terminal
os.system('cls')
# Demander le nombre d'itération à effectuer
NmbIterations = int(input(
    f'Nombre de test ? La probabilitée est de {math.factorial(len(Liste_Des_Villes)-1):_} : '))

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
    EmissionCO2Actuel = 0
    TrajetVilles = sample(
        list(zip(*Liste_Des_Villes))[0][1:], len(list(zip(*Liste_Des_Villes))[0][1:]))
    for j in range(len(TrajetVilles)):
        VilleEtape = TrajetVilles[j]
        LongueurActuelle += Distance_Villes(VilleDepart, VilleEtape)
        TrajetActuel += " -> " + VilleEtape
        EmissionCO2Actuel += EmissionCO2Calcul(
            Distance_Villes(VilleDepart, VilleEtape))
        VilleDepart = VilleEtape
    LongueurActuelle += Distance_Villes(VilleDepart, "Paris")
    TrajetActuel += " -> Paris"
    ComparaisonDistance(LongueurActuelle)
    ComparaisonEmission(EmissionCO2Actuel)
    bar.update(i)

# Calcul du temps mis pour une moyenne de 110km/h
TempsTrajet = round(LongueurMin/110)

# Récuperer le temps final et trouver le delta
EndTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
DeltaTime = EndTime - StartTime
# Convertir en minute si necessaire
if DeltaTime.total_seconds() > 60:
    DeltaTimeMin = DeltaTime.total_seconds()/60
    FinalMessage = f'Le trajet minimum est : {TrajetMin} avec {round(LongueurMin)} km       \nLa durée du voyage est de {TempsTrajet} heures.\r\nCela a pris {DeltaTimeMin} minutes'
else:
    FinalMessage = f'Le trajet minimum est : {TrajetMin} avec {round(LongueurMin)} km       \nLa durée du voyage est de {TempsTrajet} heures.\r\nCela a pris {DeltaTime.total_seconds()} secondes'

# Donner le resultat trajet et km final
print(FinalMessage)
print(
    f"L'emission CO2 est de {EmissionCO2Min:_}kg avec un parcours de {TrajetEmissionC02}")