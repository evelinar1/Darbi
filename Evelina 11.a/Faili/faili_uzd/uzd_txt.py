# Uzd1 - ierakstīt tekstu failā ar input metodi,

faila_nosaukums = 'ieraksts.txt'
def ieraksts_faila():
    with open (faila_nosaukums,'a',encoding='utf8') as file:
        for i in range (1,7):
            vards = input(f"Ievadi {i}.vārdu:")
            file.write(vards+"\n")
    print(f"Ieraksts tika saglabāts failā {faila_nosaukums}.")

#ieraksts_faila()

# Uzd2 - nolasīt tekstu no faila, ja nav atrasts fails - informēt
'''def nolasit_no_faila():
    try: 
        with open(faila_nosaukums,'r',encoding='utf8') as file:
            saturs = file.read()
            print("Faila saturs: ")
            print(saturs)
    except FileNotFoundError:
        print("Fails netika atrasts.")'''

#nolasit_no_faila()

def nolasit_ar_for(): # Nolasa informāciju no faila izmantojot for ciklu
    try:
        with open(faila_nosaukums,'r',encoding='utf8') as file:
            print("Faila saturs:")
            for i in file:
                print(i.strip()) # Noņem liekās rindas
    except FileNotFoundError:
        print("Fails netika atrasts.")

#nolasit_ar_for()

# Uzd3 - Izveidot sarakstu ar 3 vārdiem
# Pievienot šo sarakstu failiem
# Parādīt konsolē cik vārdi ir pievienoti

faila2_nosaukums = 'saraksts.txt'
def vardi_saraksta():
    saraksts = ['sniegs','ziema','saule']
    with open (faila2_nosaukums,'w',encoding='utf8') as file:
        for vards in saraksts:
            file.write(vards+"\n")
        vardu_skaits = len(saraksts)
        print(f"Failā tika ierakstīti {vardu_skaits} vārdi.") # {len(saraksts)}
    
#vardi_saraksta()

# Uzd4 - Ievadīt vārdu, ko meklēt failā un informēt lietotāju vai tāds ir

def atrast_vardu():
    try:
        vards = input("Ievadi vārdu:")
        with open(faila_nosaukums,'r',encoding='utf8') as file:
            saturs = file.read()
            if vards in saturs:
                print(f"Vārds {vards} ir atrasts.")
            else:
                print(f"Vārds {vards} nav atrasts.")        
    except FileNotFoundError:
        print("Fails netika atrasts.")

#atrast_vardu()

# Uzd5 - Sakārtot failā esošos datus dalistošā secībā

def sakartoti_dati():
    try:
        with open (faila_nosaukums,'r',encoding='utf8') as file:
            saturs = file.readlines()
            kartots = sorted(saturs,reverse=True) # Sakārto pretēji alfabēta secībai
            # Ieraksta atpakaļ failā
            with open (faila_nosaukums,'w',encoding='utf8') as file:
                file.writelines(kartots)
            print("Fails sakārtots dilstošā secībā.")
    except FileNotFoundError:
        print("Fails netika atrasts.")

sakartoti_dati()
                

    

    





        
