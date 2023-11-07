lietotajvards = 'skolens'
parole = 12345

   
lietotajvards = input("Lūdzu ievadiet lietotājvārdu:")
parole = int(input("Lūdzu ievadiet paroli:"))

if lietotajvards == 'skolens' and parole == 12345:
    print("Pieslēgšanās veiksmīga!")
else:
    for reizes in range(4):#programma atkārtojas vēl 4 reizes, ja nepieciešams
        print("Lietotājvārds vai/un parole nepareiza!")
        lietotajvards = input("Lūdzu ievadiet lietotājvārdu:")
        parole = int(input("Lūdzu ievadiet paroli:"))
    print("Iespējami tikai 5 mēģinājumi.")
    exit()#kad visi mēģinājumi izmantoti, programma beidzas

skaitlis1 = int(input("Ievadi pirmo skaitli:"))
skaitlis2 = int(input("Ievadi otro skaitli:"))

while skaitlis1 <1 or skaitlis2 <1 or skaitlis1 <1 and skaitlis2 <2:#pārbauda vai skaitlis ir pozitīvs
    print("Skaitlim jābūt pozitīvam!")#programma atkārtojas kamēr lietotājs ievada derīgus skaitļus
    skaitlis1 = int(input("Ievadi pirmo skaitli:"))
    skaitlis2 = int(input("Ievadi otro skaitli:"))
if skaitlis1 > skaitlis2:
    print("0")
    exit()

summa = sum(range(skaitlis1,skaitlis2+1))#ievadīto skaitļu range summa
print("Summa:",summa)
