saraksts = []
skaits = int(input("Cik skaitļus Jūs vēlaties ielikt sarakstā?:"))

if skaits == 3 or skaits > 3:
     for reizes in range(skaits):
            skaitlis = int(input("Ievadiet skaitli:"))
            saraksts.append(skaitlis)
else:
    while skaits < 3:
        print("Skaitlis nedrikst būt mazāks par 3!")
        skaits = int(input("Cik skaitļus Jūs vēlaties ielikt sarakstā?:"))
    else:
        skaits == 3 or skaits > 3
        for reizes in range(skaits):
            skaitlis = int(input("Ievadiet skaitli:"))
            saraksts.append(skaitlis)
print("Saraksts ar skaitļiem:", saraksts)
print("Lielākais skaitlis ir",max(saraksts))





