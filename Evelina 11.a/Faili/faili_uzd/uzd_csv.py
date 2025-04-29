# Uzd1 - Funkcija, kas izveido csv failu un ieraksta 3 rindas
import csv
faila_nosaukums = 'dati1.csv'

def izveidot_csv():
    with open (faila_nosaukums,'w',newline='',encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID","Vārds","Vecums"]) # Galvene
        writer.writerows([[1,"Alise",25],[2,"Jānis",28],[3,"Ieva",26]])
        print("Fails ir izveidots.")

izveidot_csv()

# Uzd2 - Parādīt csv faila saturu

def paradit_saturu():
    try:
        with open (faila_nosaukums,'r',newline='',encoding='utf8') as file:
            reader = csv.reader(file)
            for line in reader:
                print(*line) # * Noņem komatus un kvadrātiekavas
    except FileNotFoundError:
        print("Fails netika atrasts.")

paradit_saturu()

# Uzd3 - Pievienot jaunu id, vardu, vecumu ar input

def pievienot_datus():
    try:
        with open (faila_nosaukums,'a',newline='',encoding='utf8') as file:
            writer = csv.writer(file)
            id = int(input("Ievadiet ID numuru: "))
            vards = input("Ievadiet vardu: ")
            vecums = int(input("Ievadiet vecumu: "))
            writer.writerow([id,vards,vecums])
        print("Fails ir atjaunināts.")
    except FileNotFoundError:
        print("Fails netika atrasts.")

pievienot_datus()

           


