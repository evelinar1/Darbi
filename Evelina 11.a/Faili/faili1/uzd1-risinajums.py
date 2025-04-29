# Nolasīt csv faila saturu, aprēķināt vidējo vērtējumu
# Pievienot jaunu lauku 'vidējais', to visu saglabā jaunā csv failā

import csv
ievades_dati = 'skoleni.csv'
izvades_dati = 'skoleni_videjais.csv'

with open(ievades_dati,'r',encoding='utf8') as file: # Mainīgais file tagad attēlo atvērto failu
    # Nolasa csv failu un katru rindiņu pārvērš par vārdnīcu (kolonna - atslēga, vērtība - konkrētā rinda)
    reader = csv.DictReader(file)
    skoleni = list(reader) # Mainīgais skolēni ir python saraksts
    # Katrs saraksta elements ir 1 ieraksts no csv faila

# Rēķina vidējo un pievieno jaunu lauku
for skolens in skoleni:
    matematika = int(skolens['Matemātika'])
    anglu_valoda = int(skolens['Angļu valoda'])
    biologija = int(skolens['Bioloģija'])
    videjais = round((matematika+anglu_valoda+biologija)/3,2)
    # Katram skolēnam pievieno jaunu lauku vidējais
    skolens['Vidējais'] = videjais

# Saglabāt datus jaunā failā
with open(izvades_dati,'w',encoding='utf8',newline='') as file:
    fieldnames = skoleni[0].keys() # Atgriež pirmās kolonnas atslēgas nosaukumu
    # Objekts, kas raksta datus uz csv failu
    writer = csv.DictWriter(file,fieldnames=fieldnames) # Rakstīs pareizā secībā
    # Ieraksta pirmo rindu, kas ir kolonnu nosaukumi
    writer.writeheader() 
    writer.writerows(skoleni) # Iziet cauri sarakstam un katru vārdnīcu ieraksta kā jaunu rindu

print(f"Jaunais fails ir saglabāts kā '{izvades_dati}'.")


    



