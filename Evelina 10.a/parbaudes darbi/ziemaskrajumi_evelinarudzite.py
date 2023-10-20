aboli = float(input("Cik daudz ābolu jums ir?(kg):"))
cukurs = ['parasto','ievārijuma']
cukurs = str(input("Vai Jūs izmantosiet parasto vai ievārijuma cukuru?:"))
if cukurs == 'ievārijuma':
    cukura_cena = 2.59
elif cukurs == 'parasto':
    cukura_cena = 1.35
citrons = str(input("Vai jums ir citrons?(jā/nē):"))
if citrons == 'nē':
    citrona_cena = 0.39
mandelu_ekstrakts = str(input("Vai jums ir mandeļu ekstrakts?(jā/nē:)"))
if mandelu_ekstrakts == 'nē':
    mandelu_ekstrakta_cena = 2.90
kanelis = str(input("Vai jums ir kanēlis?(jā/nē):"))
if kanelis == 'nē':
    kanela_cena = 1.19

print("Recepte:")
print("Āboli:",aboli,"kg")
if aboli < 3:
    cukura_daudzums = (1/aboli)
    udens = (0.5/aboli)
    citroni = (1/aboli)
elif aboli > 3:
    cukura_daudzums = (1/3*aboli)
    udens = (0.5/3*aboli)
    citroni = (1/3*aboli)
print("Cukurs:","%.2f"%cukura_daudzums,"kg")
cukura_summa = (cukura_daudzums*cukura_cena)
print("Cukura cena:","%.2f"%cukura_summa,"eiro")
print("Ūdens:","%.2f"%udens,"litri")
print("Citroni:","%.2f"%citroni,"gab")
if citrons == 'nē':
    citrona_summa = (citroni*citrona_cena)
print("Citrona cena:","%.2f"%citrona_summa,"eiro")



    

