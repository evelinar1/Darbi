def parbaudit_vardu(vards): #Pārbauda, vai vārds vai uzvārds ir derīgs (sastāv tikai no burtiem un nav tukšs).
    if not vards.isalpha():
        print("Vārdā drīkst būt tikai burti!")
        return False 
    return True

def validet_vecumu(vecums):
    if not vecums.isdigit():
        print("Vecumam jābūt skaitlim!")
        return False
    if int(vecums) < 0:
        print("Vecumam jābūt lielākam par 0!")
        return False
    return True

def normalizet_vardu(vards):
    return vards.strip().capitalize() # noņem liekās atstarpes un uzliek lielo sākuma burtu

def dublikats(vards,uzvards,vecums,faila_nosaukums):
    try:
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            dati = fails.readlines()
        ieraksts = f"{vards},{uzvards},{vecums}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False # Fails nav izveidots, tātad dublikātu nav

def pievienot_datus_failam(faila_nosaukums):
    #Pievieno datus failā pēc validācijas.
    try:
        with open(faila_nosaukums, "a", encoding="utf-8") as fails:
            while True:
                vards = input("Ievadiet vārdu: ")
                if parbaudit_vardu(vards):
                    vards = normalizet_vardu(vards)
                    break     

            while True: 
                uzvards = input("Ievadiet uzvārdu: ")
                if parbaudit_vardu(uzvards):
                    uzvards = normalizet_vardu(uzvards)
                    break

            while True:
                vecums = input("Ievadiet vecumu: ")
                if validet_vecumu(vecums):
                    break

            if dublikats(vards,uzvards,vecums,faila_nosaukums):
                print("Šis ieraksts jau pastāv!")
                return

            fails.write(f"{vards},{uzvards},{vecums}\n")
        print("Dati veiksmīgi pievienoti failam.")
    except Exception as e:
        print(f"Kļūda, saglabājot datus failā: {e}")

def paradit_datus(faila_nosaukums):
    #Parāda datus no faila, ja tāds eksistē un nav tukšs.
    try:
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            dati = fails.readlines()

        if not dati:
            print("Fails ir tukšs. Lūdzu, pievienojiet datus vispirms.")
        else:
            print("\nDati no faila:")
            for ieraksts in dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails '{faila_nosaukums}' nepastāv. Lūdzu, pievienojiet datus vispirms.")

def iegut_vecumu_no_datiem(ieraksts):
    #Izvelk vecumu no datu ieraksta.
    try:
        vecums = int(ieraksts.strip().split(",")[-1])
        return vecums
    except (IndexError, ValueError):
        return 0  # Ja formāts nav pareizs, atgriež 0

def sakartot_un_paradit_datus(faila_nosaukums):
    #Sakārto datus pēc vecuma un parāda tos konsolē.
    try:
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            dati = fails.readlines()

        if not dati:
            print("Fails ir tukšs. Lūdzu, pievienojiet datus vispirms.")
        else:
            # Kārtošana pēc vecuma
            sakartoti_dati = sorted(dati, key=iegut_vecumu_no_datiem)

            print("\nDati, sakārtoti pēc vecuma:")
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails '{faila_nosaukums}' nepastāv. Lūdzu, pievienojiet datus vispirms.")

def izvelne():
    #Parāda izvēlni un apstrādā lietotāja izvēli.=
    faila_nosaukums = "dati.txt"

    while True:
        print("\nIzvēlieties opciju:")
        print("1 - Pievienot datus")
        print("2 - Parādīt datus")
        print("3 - Parādīt sakārtotus datus pēc vecuma")
        print("4 - Iziet")

        izvēle = input("Izvēle: ")

        if izvēle == "1":
            pievienot_datus_failam(faila_nosaukums)
        elif izvēle == "2":
            paradit_datus(faila_nosaukums)
        elif izvēle == "3":
            sakartot_un_paradit_datus(faila_nosaukums)
        elif izvēle == "4":
            print("Izvade tiek pārtraukta.")
            break
        else:
            print("Nepareiza izvēle. Lūdzu, mēģiniet vēlreiz.")

# Galvenā programmas izsaukšana
izvelne()
#faila_nosaukums tiek padots kā arguments, lai funkcijas būtu atkārtoti izmantojamas ar citiem failiem.
#Katra datu rinda ir atdalīta ar komatiem (vārds,uzvārds,vecums), kas atvieglo datu apstrādi.
#sakartot_un_paradit_datus() izmanto iegut_vecumu_no_datiem() funkciju, lai iegūtu vecumu no katras rindas un sakārtotu pēc tā.