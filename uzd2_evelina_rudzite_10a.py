temperatura = {
    "1.decembris":3,
    "2.decembris":6,
    "3.decembris":4,
    "4.decembris":8,
    "5.decembris":3,
    "6.decembris":2,
    "7.decembris":6    
}

datums = input("Ievadiet datumu(piemēram, 1.decembris):")
gradi = temperatura[datums]
farenheits = (gradi*(9/5)+32)

if datums in temperatura:
    print(datums,"temperatūra Celsija skalā ir:",gradi,"grādi.")
    farenheits = (gradi*(9/5)+32)
    print("---")
    print(datums,"temperatūra Fārenheita skalā ir:", farenheits,"grādi")
'''else:
    datums not in temperatura:
        for reizes in range(3):
        print("Datums nepareizs!Ievadiet datumu skalā no 1-7:")
        datums = input("Ievadiet datumu(piemēram, 1.decembris):")   
    print(datums,"temperatūra Celsija skalā ir:",gradi,"grādi.")'''





