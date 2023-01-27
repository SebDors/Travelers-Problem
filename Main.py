import numpy as np
import math as math
from datetime import datetime

# Création d'un tableau contenant les villes et leurs coordonnées géographique
Liste_Des_Villes = [["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg"],
                    [48.8566, 43.2965, 45.764, 43.6047, 43.7101, 47.2184, 48.5734],
                    [2.3522, 5.3698, 4.8357, 1.4442, 7.262, -1.5536, 7.7521],
                    [0,       0,     0,     0,       0,         0,     0]]


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
    LongA, LongB = LongVille(VilleA), LongVille(VilleB)
    LatA, LatB = LatVille(VilleA), LatVille(VilleB)
    LongA, LongB = math.radians(LongA), math.radians(LongB)
    LatA, LatB = math.radians(LatA), math.radians(LatB)
    return Rayon*(np.arccos(np.sin(LatA)*np.sin(LatB)+np.cos(LatA)*np.cos(LatB)*np.cos(LongB-LongA)))


# Initialisation des variables générales
LongueurMin = 2_147_483_647  # Valeure maximum que peut comporter un integer
TrajetMin = ""
# Demander le nombre d'itération à effectuer
NmbIterations = int(input("Number of iterations ?"))


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


def Reset():
    """
    Remettre le nombre de passages des villes à 0
    Entree : None
    Return : None
    """
    for i in range(0, len(Liste_Des_Villes[3])):
        Liste_Des_Villes[3][i] = 0


# Récuperer le temps du start
StartTime = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
print(f'Départ de la simulation: {StartTime}')
for i in range(NmbIterations):
    VilleDépart = "Paris"
    LongueurActuelle = 0
    TrajetActuel = VilleDépart
    Reset()
    while Liste_Des_Villes[3][0] == 0:
        # Choix de la prochaine destination
        ChoixDeVille = np.random.randint(1, (len(Liste_Des_Villes[0])))

        while Liste_Des_Villes[3][ChoixDeVille] == 1:
            # Check si nous n'avons pas pris une destination déjà prise
            ChoixDeVille = np.random.randint(1, (len(Liste_Des_Villes[0])))
        VilleEtape = Liste_Des_Villes[0][ChoixDeVille]

        # Ajouter un 1 pour prevenir que nous sommes déjà passé par cette destination
        Liste_Des_Villes[3][ChoixDeVille] = 1
        # Mettre à jour la distance actuelle
        LongueurActuelle += Distance_Villes(VilleDépart, VilleEtape)/1000

        # Integrer les étapes dans notre Trajet actuelle
        TrajetActuel += " -> " + VilleEtape
        # Intervertir Ville de départ et ville d'arrivée
        VilleDépart = VilleEtape

        # Checker si nous n'avons pas fais toutes les destinations
        # Additionner la dernière ligne de toutes les villes pour savoir si nous sommes passé par toutes proposées
        count = 0
        for j in range(len(Liste_Des_Villes[3])):
            x = Liste_Des_Villes[3][j]
            count += x
            # print(count)

        # Comparer le nombres de villes traversés avec le nombre total possible
        if count == (len(Liste_Des_Villes[3])-1):
            # Passer de la dernière ville à Paris (Ville de fin)
            LongueurActuelle += Distance_Villes(VilleDépart, "Paris")/1000
            TrajetActuel += " -> Paris"
            # Spécifier que nous sommes passé par Paris
            Liste_Des_Villes[3][0] = 1
            break
    ComparaisonDistance(LongueurActuelle)

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
