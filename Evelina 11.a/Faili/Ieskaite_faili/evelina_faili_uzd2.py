import csv

# 1. Uzdevums

faila_nosaukums = 'pilsetas2.csv'

def ierakstit_informaciju():
    with open (faila_nosaukums,'w',newline='',encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nosaukums','Iedzīvotāju skaits']) # Izveido galveni
        writer.writerows([['Sigulda',9324],['Rīga',453455],['Cēsis',34234],['Ogre',5433],['Jelgava',45343]])
    print(f"Informācija pievienota failam: {faila_nosaukums}")

#ierakstit_informaciju()

# 2. Uzdevums

def paradit_pilsetas():
    try:
        with open (faila_nosaukums,'r',newline='',encoding='utf8') as file:
            reader = csv.reader(file)
            for line in reader:
                #print(f"Pilseta: {line[0]}, iedzivotaju skaits: {line[1]}.")
                print(*line) # Noņem kvadrātiekvas un liekos komatus
                print('------------')
    except FileNotFoundError:
        print("Fails netika atrasts.")

#paradit_pilsetas()

# 3. Uzdevums

'''def iedzivotaju_sk_summa():
    try:
        with open (faila_nosaukums,'r',newline='',encoding='utf8') as file:
            reader = csv.reader(file)
            for i in reader:
                summa = sum(file['Iedzīvotāju skaits'])
            print(summa)
    except FileNotFoundError:
        print("Fails netika atrasts.")

iedzivotaju_sk_summa()'''





