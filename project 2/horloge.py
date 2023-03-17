# import time
# time, qui fournit de fonctionnalitéspour travailler avec le date et heure
# # dans ma fonction afficher_heur La fonction prend en paramétre un tuple contenant l'heure les minutes et les secondes
# def afficher_heur(heure):
#     # Cette syntaxe permet de garantir que l'heure affichée aura toujours deux chiffres pour les heures, les minutes et les secondes.
#     heures, minutes, secondes = heure
#     # ensuite je demande a le print
#     print(f"{heures:02}:{minutes:02}:{secondes:02}:")



import time
# # time, qui fournit de fonctionnalitéspour travailler avec le date et heure
# def afficher_heure(heure):
#     # dans ma fonction afficher_heur La fonction prend en paramétre un tuple contenant l'heure les minutes et les secondes
#     heures, minutes, secondes = heure
#     # Cette syntaxe permet de garantir que l'heure affichée aura toujours deux chiffres pour les heures, les minutes et les secondes.
#     print(f"{heures:02}:{minutes:02}:{secondes:02}")
#     # ensuite je demande a le print

def heure_choisi():
    ver = input("am/pm?    Y/N :")
    hh = int(input("heures : "))
    mm = int(input("minutes :"))
    ss = int(input("secondes :"))
    while True:
        ss += 1
        if ss == 60:
            ss = 0
            mm += 1
        if mm == 60:
            mm = 0
            hh += 1
        if hh == 24:
            hh = 0
        time.sleep(0.96) #le temps d'une seconde avec les étapes
        if ver.upper() == "Y":
            print(str((hh-1)%12 +1)+":"+str(mm)+":"+str(ss) + ["AM", "PM"][hh//12])
        else:
            print(str(hh)+":"+str(mm)+":"+str(ss))
heure_choisi()

# def regler_alarme(heure_alarme):
#     while True:
#         heure_actuelle = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
#         if heure_actuelle == heure_alarme:
#             print("Alarme !")
#         time.sleep(1)

# heure_actuelle = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
# #afficher_heure(heure_actuelle)

# while True:
#     heure_actuelle = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
#     afficher_heure(heure_actuelle)
#     time.sleep(1)

