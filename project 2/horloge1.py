import time

def afficher_heure(heure, mode_24h=True):
    while True:
        # Récupérer l'heure actuelle
        heure_actuelle = time.localtime()
        heure_actuelle_str = time.strftime("%H:%M:%S", heure_actuelle)

        # Convertir l'heure au format 12 heures si nécessaire
        if not mode_24h:
            heure_actuelle_str = time.strftime("%I:%M:%S %p", heure_actuelle)

        # Afficher l'heure actuelle
        print(heure_actuelle_str, end='\r')

        # Attendre une seconde
        time.sleep(1)

def regler_heure():
    heures = int(input("Heures : "))
    minutes = int(input("Minutes : "))
    secondes = int(input("Secondes : "))
    heure = (heures, minutes, secondes)
    return heure

def regler_alarme():
    heures = int(input("Heures : "))
    minutes = int(input("Minutes : "))
    secondes = int(input("Secondes : "))
    alarme = (heures, minutes, secondes)
    return alarme

def choisir_mode_affichage():
    while True:
        choix = input("Choisir un mode d'affichage (12 heures/24 heures) : ")
        if choix == "12 heures":
            return False
        elif choix == "24 heures":
            return True
        else:
            print("Veuillez choisir un mode d'affichage valide.")

def mettre_en_pause():
    input("Appuyez sur une touche pour reprendre l'horloge...")

heure = regler_heure()
alarme = regler_alarme()
mode_24h = choisir_mode_affichage()
afficher_heure(heure, mode_24h)