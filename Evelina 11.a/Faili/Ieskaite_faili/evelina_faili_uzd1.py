# 1. Uzdevums

faila_nosaukums = 'pilsetas.txt'
def ierakstit_pilsetas():
    with open (faila_nosaukums,'w',encoding='utf8') as file:
            for i in range (1,11): # Ļaus ierakstīt pilsētas 10x
                pilseta = input(f"Ievadiet {i}. pilsētas nosaukumu: ") 
                file.write(pilseta+'\n') # Ieraksta pilsētu nosaukumus failā stabiņā uz leju
            print(f"Ieraksti tika saglabāti failā: {faila_nosaukums}.")
        

#ierakstit_pilsetas()

# 2. Uzdevums

def nolasit_informaciju():
    try:
        with open(faila_nosaukums,'r',encoding='utf8') as file:
            for i in file:
                print(i.strip()) # Noņem liekās rinas 
            print("--------------")
    except FileNotFoundError: # Kļūdas paziņojums, ja fails netiek atrasts
        print("Fails netika atrasts.")

#nolasit_informaciju()

# 3. Uzdevums

def sakartotas_pilsetas():
    try:
        with open(faila_nosaukums,'r',encoding='utf8') as file:
            saturs = file.readlines()
            sakartots = sorted(saturs) # Sakārto alfabēta secībā
        print(*sakartots) # Noņem kvadrātiekavas
    except FileNotFoundError: 
        print("Fails netika atrasts.")

#sakartotas_pilsetas()

# 4. Uzdevums

def pievienot_pilsetas():
    while True:
        try:
            for i in range(1,4):
                pilseta = input(f"Ievadi {i}. Pilsētas nosaukumu:")
                with open(faila_nosaukums,'r',encoding='utf8') as file:
                    saturs = file.read()
                    if pilseta in saturs:
                        print(f"pilsēta: {pilseta} jau eksistē failā.")
                        break
                    else:
                        with open(faila_nosaukums,'a',encoding='utf8') as file:
                            file.write(pilseta)  
                            print("Pilsētu nosaukumi tika saglabāti failā.")    
                            break     
        except FileNotFoundError:
            print("Fails netika atrasts.")
    

pievienot_pilsetas()