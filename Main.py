# Import des bibliothèques nécessaires
import math as math
from datetime import datetime
from random import shuffle
from progressbar import ProgressBar, Percentage, Timer, Bar, ETA
import os

# Création d'un tableau contenant les villes et leurs coordonnées géographique
STARTCITY="Paris"
Liste_Des_Villes = {
    # Nom de la ville: [ Latitude, Longitude]
    STARTCITY: [ 48.8566, 2.3522],
    "Marseille": [ 43.2965, 5.3698],
    "Lyon": [ 45.764, 4.8357],
    "Toulouse": [ 43.6047, 1.4442],
    "Nice": [ 43.7101, 7.262],
    "Nantes": [ 47.2184, -1.5536],
    "Strasbourg": [ 48.5734, 7.7521],
    "Montpellier": [ 43.6107, 3.8767],
    "Bordeaux": [ 44.8379, -0.5795],
    "Lille": [ 50.6329, 3.0583],
    "Rennes": [ 48.1134, -1.6779],
    "Grenoble": [ 45.1885, 5.7245],
    "Rouen": [ 49.4431, 1.0989],
    "Saint-Etiennes": [ 45.4386, 4.3871],
    "Dijon": [ 47.3167, 5.0167],
    "Nimes": [ 43.8345, 4.3600],
    "Villeurbannes": [ 45.7644, 4.8864],
    "Angers": [ 47.4784, -0.5602],
    "Saint-Denis": [ 48.9358, 2.3596],
    "Aix-en-Provence": [ 43.5297, 5.4474],
    "Brest": [ 48.3893, -4.486],
    "Limoges": [ 45.8319, 1.2621],
    "Clermont-Ferrand": [ 45.7833, 3.0833],
    "Amiens": [ 49.8941, 2.295],
    "Nancy": [ 48.6839, 6.1844],
    "Roubaix": [ 50.6942, 3.1746],
    "Tourcoing": [ 50.7236, 3.1524],
    "Orléans": [ 47.9029, 1.9107],
    "Mulhouse": [ 47.7500, 7.3335],
    "Caen": [ 49.1828, -0.3715]
}

# Selectionner uniquement la première colonne
villeNames = list(Liste_Des_Villes.keys())

# Convert all cities position to radian
radVilles = {}
for villename in villeNames:
    radVilles[villename] = [ math.radians(Liste_Des_Villes[villename][0]),math.radians(Liste_Des_Villes[villename][1])]


def cls():
    print("\033[H\033[J", end="")



def Distance_Villes(VilleA, VilleB,cached=True):
    """
    Fonction permettant de calculer la distance entre deux villes

    Entree : VilleA,VilleB 'string'
    Return : Distance 'int'
    """
    global cached_distances

    if cached:
        lvilles = []
        lvilles.append(VilleA)
        lvilles.append(VilleB)
        lvilles.sort()
        kvilles = "-".join(lvilles)
        dist = cached_distances[kvilles]
    else:
        Rayon = 6_367_445
        LatA, LatB = radVilles[VilleA][0],radVilles[VilleB][0] 
        LongA, LongB = radVilles[VilleA][1],radVilles[VilleB][1] 
        dist = round((Rayon*(math.acos(math.sin(LatA)*math.sin(LatB)+math.cos(LatA)*math.cos(LatB)*math.cos(LongB-LongA))))/1000)

    return dist


# Initialisation des variables générales
# Valeure maximum que peut comporter un integer
LongueurMin = float("inf")
TrajetMin = []

# Clear le terminal
cls()

# Demander le nombre d'itération à effectuer
maxNbIterations = math.factorial(len(Liste_Des_Villes)-1)
inputValue = input(
    f'Nombre de test ? La probabilitée est de [{maxNbIterations}] : ')

if inputValue:
    NmbIterations = int(inputValue)
else:
    NmbIterations = maxNbIterations


# Fonction pour comparer la distance actuelle avec la distance minimale
def ComparaisonDistance(dist):
    global LongueurMin
    global TrajetMin
    global VilleEtapes

    # Si la distance actuelle est plus courte que la distance minimale
    # Alors la distance minimale est mise à jour
    if dist < LongueurMin:
        LongueurMin = dist
        TrajetMin = VilleEtapes.copy()


# Compute all cities distances
def compute_cached_distances():
    global cached_distances

    for villeA in villeNames:
        for villeB in villeNames:
            if villeA==villeB:
                continue

            lvilles = []
            lvilles.append(villeA)
            lvilles.append(villeB)
            lvilles.sort()
            kvilles = "-".join(lvilles)
            if kvilles not in cached_distances:
                cached_distances[kvilles] = Distance_Villes(villeA, villeB,cached=False)

cached_distances = {}
compute_cached_distances()

# Récuperer le temps du début de la simulation
StartTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
# Début de la barre de progression
bar = ProgressBar(widgets=[Percentage(), Timer(),
                           Bar(), ETA()], maxval=NmbIterations)
bar.start()
# Boucle principale pour effectuer le nombre d'itérations demandé
for i in range(NmbIterations):
    # Initialisation de la distance actuelle et ville de départ
    LongueurActuelle = 0
    VilleEtapes = [STARTCITY]

    # Sélectionner aléatoirement les villes à visiter parmi la première colonne deu tableau des villes
    shuffle(villeNames)
    # Boucle pour visiter les villes sélectionnées
    for vname in villeNames:
        if vname == STARTCITY:
            continue

        VilleEtapes.append(vname)

        nbEtapes = len(VilleEtapes)
        LongueurActuelle += Distance_Villes(VilleEtapes[nbEtapes-2], VilleEtapes[nbEtapes-1])

    # Ajouter la distance de la dernière ville à Paris
    VilleEtapes.append(STARTCITY)
    nbEtapes = len(VilleEtapes)
    LongueurActuelle += Distance_Villes(VilleEtapes[nbEtapes-2], VilleEtapes[nbEtapes-1])

    # Appeler la fonction pour comparer la distance actuelle avec la distance minimale
    ComparaisonDistance(LongueurActuelle)
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
    FinalMessage = f'Le trajet minimum est :  avec {round(LongueurMin)} km       \nLa durée du voyage est de {TempsTrajet} heures.\r\nCela a pris {DeltaTimeMin} minutes'
else:
    FinalMessage = f'Le trajet minimum est :  avec {round(LongueurMin)} km       \nLa durée du voyage est de {TempsTrajet} heures.\r\nCela a pris {DeltaTime.total_seconds()} secondes'

# Donner le resultat trajet et km final
cls()
print(" => ".join(VilleEtapes))
print(
    f'{NmbIterations} itérations avec {round(LongueurMin)} km       \nLa durée du voyage est de {TempsTrajet} heures.\r\nCela a pris {DeltaTime.total_seconds()} secondes')
