# Import des bibliothèques nécessaires
import numpy as np
import math as math
from datetime import datetime
from random import sample
from progressbar import ProgressBar, Percentage, Timer, Bar, ETA
import os
import TSP_Lib

# Création d'un tableau contenant les villes et leurs coordonnées géographique
Liste_Des_Villes = [
    # [Nom de la ville, Latitude, Longitude]
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

# Initialisation des variables générales
# Valeure maximum que peut comporter un integer
LongueurMin = float("inf")
TrajetMin = ""
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
# Boucle principale pour effectuer le nombre d'itérations demandé
for i in range(NmbIterations):
    # Initialisation de la distance actuelle
    LongueurActuelle = 0
    # Initialisation de la ville de départ
    VilleDepart = "Paris"
    TrajetActuel = VilleDepart
    # Sélectionner aléatoirement les villes à visiter
    TrajetVilles = sample(list(zip(*Liste_Des_Villes))
                          [0][1:], len(list(zip(*Liste_Des_Villes))[0][1:]))
    # Boucle pour visiter les villes sélectionnées
    for j in range(len(TrajetVilles)):
        VilleEtape = TrajetVilles[j]
        LongueurActuelle += TSP_Lib.Distance_Villes(
            VilleDepart, VilleEtape, Liste_Des_Villes)
        TrajetActuel += " -> " + VilleEtape
        VilleDepart = VilleEtape
    # Ajouter la distance de la dernière ville à Paris
    LongueurActuelle += TSP_Lib.Distance_Villes(VilleDepart,
                                                "Paris", Liste_Des_Villes)
    TrajetActuel += " -> Paris"
    # Appeler la fonction pour comparer la distance actuelle avec la distance minimale
    LongueurMin, TrajetMin = TSP_Lib.comparaison(
        LongueurActuelle, LongueurMin, TrajetMin, TrajetActuel)
    # Mettre à jour la barre de progression
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
