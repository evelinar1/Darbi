import csv

def izveidot_failu():
    with open('pilsetas3.csv','w',newline='',encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nosaukums','Iedzīvotāju skaits'])
        for i in range(5):
            while True:
                pilseta = input(f"Ievadiet {i+1}. pilsētas nosaukumu:")
                if pilseta:
                    try:
                        iedzivotaji = int(input(f"ievadiet '{pilseta}'iedzīvotāju sakitu: "))
                        writer.writerow([pilseta,iedzivotaji])
                        break
                    except ValueError:
                        print("Lūdzu, ievadiet skaitli!")
                else:
                    print("Pilsētas nosaukums nedrīkst būt tukšs!")

izveidot_failu()

def summa():
    try:
        with open ('pilsetas3.csv','r',newline='',encoding='utf8') as file:
            lasitajs = csv.reader(file)
            next(lasitajs)
            kop_skaits = sum(int(rinda[1])for rinda in lasitajs)
        print(f"Kopējais skaits: {kop_skaits}")
    except FileNotFoundError:
        print("Fails netika atrasts.")

summa()


