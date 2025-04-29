# Funkcija, kas nodrošina lietotāja datu ievadi
def datu_ievade():
    # Izveido tukšus sarakstus, kuros saglabās lietotāja ievadīto informāciju
    laiki = []
    cenas = []
    marsruts = []
    transporti = []
    attalumi = []

    while True:
        try:
            skolenu_skaits = int(input('Ievadiet cilvēku skaitu: '))
            if skolenu_skaits <= 0: # Pārbauda lai ievadītais skolēnu skaits ir pozitīvs un nav 0
                print('Ievadiet derīgu vērtību!')
                continue
            break
        except ValueError: # Kļūdu pārbaude - pārbauda vai ievadītā vērtība atbilst prasītajam
            print('Ievadiet derīgu vērtību!')
    
    while True:
        pilsetas_pieturas = input('Ievadiet pieturu (lai beigtu ievadi - stop): ')
        if pilsetas_pieturas == 'stop': # Ja ievadīts 'stop', lietotājs beidz ievadīt pilsētu / pieturu nosaukums
            break
        marsruts.append(pilsetas_pieturas) # Pievieno ievadīto pilsētu / pieturu nosaukumus tukšajam sarksatam
        
    for i in range (len(marsruts)): # Izmantojot 'len' saskaita cik ir pieturas un ļauj lietotājam ievadīt informāciju par katru pieturu
        while True:
            try:
                transporta_veids = int(input(f'Izvēlaties transporta veidu uz {marsruts[i]} (1 - Autobuss, 2 - Vilciens, 3 - Kājām):')) # '{marsruts[i]}' norāda par kuru pieturu tiek ievadīta informācija
                if transporta_veids not in [1, 2, 3]: # Pārbauda vai ir ievadīta viena no dotajām vērtībām
                    print('Ievadiet derīgu vērtību!')
                    continue
                if transporta_veids == 1: # Sarakstā ievada transporta veida nosaukumu atbilstoši ievadītajam ciparam
                    transporti.append('Autobuss')
                elif transporta_veids == 2:
                    transporti.append('Vilciens')
                elif transporta_veids == 3:
                    transporti.append('Kājām')
                break
            except ValueError:
                print('Ievadiet derīgu vērtību!')
        
        while True:
            try:
                attalums = float(input('Ievadiet attālumu (km): '))
                attalumi.append(attalums)
                break
            except ValueError:
                print('Ievadiet derīgu vērtību!')
        while True:
            if transporta_veids == 1 or transporta_veids == 2: # Ja ievadītā atbilde ir 1 vai 2
                while True:
                    try:
                        transporta_cena = float(input('Ievadiet cenu (eiro):'))
                        cenas.append(transporta_cena)
                        break
                    except ValueError:
                        print('Ievadiet derīgu vērtību!')
                while True:
                    try:
                        laiks = int(input('Ievadiet laiku (min):'))
                        laiki.append(laiks)
                        break
                    except ValueError:
                        print('Ievadiet derīgu vērtību!')
            else: # Ja ievadītā atbilde ir 3
                cenas.append(0) # Pievieno sarakstam 0 eiro, jo par iešanu ar kājām nav transporta maksas
                laiks = attalums/5*60 # Par cik 1h noiet 5km, veicamo attalumu dala ar 5 un pareizina ar 60 lai dabūtu laiku minūtēs
                laiki.append(laiks)
            break
        
    return laiki, cenas, attalumi, marsruts, transporti, skolenu_skaits
        


# Funkcija, kas veic aprēķinus un izvada rezultātu 
def aprekini(laiki, cenas, attalumi, transporti, marsruts, skolenu_skaits):
    kopejais_laiks = sum(laiki) # Izmantojot 'sum' aprēķina kopējo vērtību saskaitot kopā visas sarakstā esošās vērtības
    kopejais_attalums = sum(attalumi)
    kopejas_izmaksas_uz_cilveku = sum(cenas)
    kopejas_izmaksas_uz_klasi = kopejas_izmaksas_uz_cilveku * skolenu_skaits 
    # Kopsavilkums - parāda visu informāciju uz ekrāna
    print('-----Ekskurijas info-----')
    print('Maršruts: ',marsruts)
    print('Izvēlētie transporta veidi: ',transporti)
    print('Kopējais attālums: ',kopejais_attalums, 'km')
    print('Kopējais laiks: ',kopejais_laiks, 'min')
    print('Kopējā cena uz cilvēku: ',kopejas_izmaksas_uz_cilveku, 'eiro')
    print('Kopējā cena uz klasi: ',kopejas_izmaksas_uz_klasi, 'eiro')
    

# Galvenā funkcija, kas izsauc iepriekšējās funkcijas
def galvena():
    while True:
        laiki, cenas, attalumi, marsruts, transporti, skolenu_skaits = datu_ievade()
        aprekini(laiki, cenas, attalumi, transporti, marsruts, skolenu_skaits)
        
# Izsauc galveno funkciju, lai strādātu programma       
galvena()
    




                    

    
            







        
    
        


        


