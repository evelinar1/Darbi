'''>izveidot 3 sarakstus:lietotajs pats norādīs,
cik elementus likt sarakstā.
>Pirmā un otrā saraksta vērtības ievada lietotājs.
>Trešā saraksta vērtības iegūst apvienojot pirmos divus sarakstus.
>Katra saraksta saturu glīti parādīt uz ekrāna.'''
saraksts1=[]
saraksts2 = []
saraksts1_vert = int(input("Ievadiet elementu skaitu:"))
for reizes in range(saraksts1_vert):
    saraksts1_elem = input("Ievadiet saraksta elementu:")
    saraksts1.append(saraksts1_elem)
print("Pirmais saraksts: ",saraksts1)

saraksts2_vert = int(input("Ievadiet elementu skaitu:"))
for reizes in range(saraksts2_vert):
    saraksts2_elem = input("Ievadiet saraksta elementu:")
    saraksts2.append(saraksts2_elem)
print("Otrais saraksts: ",saraksts2)

saraksts3 = [saraksts1+saraksts2]
print("Trešais saraksts: ",saraksts3)




'''saraksts1 = []
saraksts2 = []
print("Ievadi saraksta garumu: ")
garums =int(input())

for i in range(garums):
    lieta1 = input("Ievadiet sarakstsa elementu:")
    saraksts1.append(lieta1)
print("Pirmā saraksta elementi:",saraksts1)'''
