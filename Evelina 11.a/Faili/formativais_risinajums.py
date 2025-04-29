def parbaudit_vardu_uzvardu(teksts):
    return teksts.isalpha() and teksts.strip() # Pārbauda vai ir tikai burti

def parbaudit_vecumu(vecums):
    return vecums.isdigit() and int(vecums)>0 # Pārbauda ierobežojumu: veseli skaitļi > 0

def parbaudit_atzimi(atzime):
    return atzime.isdigit() and 0<=int(atzime)<=10 # Atzīmes ierobežojums

def ierobezo_meginajumus(parbaudit_funkcija,ievades_teksts,kludas_teksts):
    # Ievade ar pārbaudi, kur ļauj max 3 mēģinājumus
    for i in range(3):
        dati = input(ievades_teksts)
        if parbaudit_funkcija(dati):
            return dati
        print(kludas_teksts)
    print("Pārsniegts mēģinājumu skaits!")

def iegut_ierakstu():
    ieraksti = []
    while True:
        # Vārda un uzvārda ievade un pārbaude
        vards = ierobezo_meginajumus(parbaudit_vardu_uzvardu,
        "Ievadiet vārdu: ",
        "Kļūda: Vārdā drīkst būt tikai burti.")
        if not vards:
            break

        uzvards = ierobezo_meginajumus(parbaudit_vardu_uzvardu,
        "Ievadiet Uzvārdu: ",
        "Kļūda: Uzvārdā drīkst būt tikai burti.")
        if not uzvards:
            break

        vecums = ierobezo_meginajumus(parbaudit_vecumu,
        "Ievadiet vecumu: ",
        "Kļūda: Vecums drīkst sastāvēt tikai no cipariem.")
        if not vecums:
            break

        atzime = ierobezo_meginajumus(parbaudit_atzimi,
        "Ievadiet atzīmi: ",
        "Kļūda: Atzīme drīkst sastāvēt tikai no cipariem.")
        if not atzime:
            break

        ieraksti.append((vards,uzvards,int(vecums),int(atzime)))
        turpinat = input("Vai turpināt? (j/n): ").lower()
        if turpinat == 'n': # Ja nav vienāds ar jā
            break
    return ieraksti

def saglabat_faila(ieraksti,faila_nosaukums="kontroldarbs.txt"):
    # Saglabāt ierakstus ar tabulatoriem starp laukiem
    with open (faila_nosaukums,"a",encoding='utf8') as file:
        for ieraksts in ieraksti:
            file.write("\t".join(map(str,ieraksts))+"\n")
    print(f"Dati saglabāti failā: {faila_nosaukums}.")

def paradit_sakartotus_datus(ieraksti):
    # Sakārtoti dati pēc gala atzīmes
    # Definēt anonīmo funkciju lambda, kas pieņem 1 argumentu x (katrs ieraksts no saraksta)
    sakartoti_ieraksti = sorted(ieraksti,key=lambda x:x[3])
    print("\nVārds\tUzvārds\tVecums\tAtzīme")
    for ieraksts in sakartoti_ieraksti:
        print("\t".join(map(str,ieraksts)))

# Kārtošanas opcija ar atsevišķu funkciju
'''def iegut_gala_atzimi(ieraksts):
    return ieraksts[3]

def paradit_sakartotus_datus(ieraksti):
    # Sakārtoti dati pēc gala atzīmes
    # Definēt anonīmo funkciju lambda, kas pieņem 1 argumentu x (katrs ieraksts no saraksta)
    sakartoti_ieraksti = sorted(ieraksti,key=iegut_gala_atzimi)
    print("\nVārds\tUzvārds\tVecums\tAtzīme")
    for ieraksts in sakartoti_ieraksti:
        print("\t".join(map(str,ieraksts)))'''

def izvelne(): # Programmas galvenā daļa
    ieraksti = []

    while True:
        print("\nIzvēlieties darbību:")
        print("izvēlaties darbību:\n(1) - Ievadīt datus\n(2) - Saglabāt datus failā\n(3) - Parādīt datus sakārtotus pēc gala atzīmes\n(4) - Iziet no programmas")
        izvele = input("Jūsu izvēle:")

        if izvele == '1':
            ieraksti+=iegut_ierakstu()
        elif izvele == '2':
            if ieraksti:
                saglabat_faila(ieraksti)
            else:
                print("Nav datu, ko saglabāt!")
        elif izvele == '3':
            if ieraksti:
                paradit_sakartotus_datus(ieraksti)
            else:
                print("Nav datu, ko parādīt!")
        elif izvele == '4':
            print("Programma tiek pārtraukta.")
            break
        else:
            print("Nepareiza izvēle. Lūdzu, mēģiniet vēlreiz.")

izvelne()