import csv 
# Ievietot failā 5 ierakstus, parādīt uz ekrāna 
csv_file = 'darbinieki.csv'
# Ierakstāmie dati
darbinieki = [
    {'Vārds':'Anna','Amats':'Skursteņslauķis','Alga':900},
    {'Vārds':'Liene','Amats':'Ārste','Alga':1200},
    {'Vārds':'Ilze','Amats':'Programmētāja','Alga':'skola'},
    {'Vārds':'Mārtiņš','Amats':'Grāmatvedis','Alga':950},
    {'Vārds':'Pēteris','Amats':'Direktors','Alga':1250}    
]

# Datu ierakstīšana failā

with open(csv_file,'w',encoding='utf8',newline='') as file:
    fieldnames = ['Vārds','Amats','Alga'] # Kolonnu nosaukumi
    writer = csv.DictWriter(file,fieldnames)
    writer.writeheader() # Ieraksta kolonnu galvenes
    writer.writerows(darbinieki)

# Nolasīt faila saturu un parādīt darbiniekus ar algu > 1000
try:
    with open(csv_file,'r',encoding='utf8') as file:
        reader = csv.DictReader(file)
        algas_filtrs = []
        for rinda in reader:
            try:
                alga = int(rinda['Alga'])
                if alga > 1000:
                    algas_filtrs.append(rinda)
            except ValueError:
                print(f"Brīdinājums: Rindā {rinda['Vārds']} {rinda['Amats']} nav derīga alga.")
        if algas_filtrs:
            for darbinieks in algas_filtrs:
                print(f"Vārds:{rinda['Vārds']}, Amats:{rinda['Amats']}, Alga:{rinda['Alga']}")
        else:
            print("Nav tādu darbinieku!")
            
except FileNotFoundError:
    print(f"Fails '{csv_file}' nav atrasts.")
except Exception as e:
    print(f"Kļūda nolasot failu: {e}")



'''with open (csv_file,'r',encoding='utf8') as file:
    reader = csv.DictReader(file)
    for rinda in reader:
        if int(rinda['Alga']) > 1000:
            print(f"Vārds:{rinda['Vārds']}, Amats:{rinda['Amats']}, Alga:{rinda['Alga']}")'''






    

# Pārbaudīt vai alga ir ielikts kā derīgs skaitlis
# Ja nav derīgs skaitlis, tad izdrukāt brīdinājumu
# Ja fails darbinieki.csv neeksistē, tad izdrukāt kļūdas paziņojumu

# Uzd3 - jaunā failā
# No faila skoleni.csv faila noteikt, kurš skolēns ieguvis visaugstāko vidējo vērtējumu
# Parādīt skolēna vārdu

#with open("skoleni.csv","r",encoding='utf8') as fails:
    