stop = '0'
ceks ='Iepirkšanās čeks:'#izveidots lai nebūtu katru reizi jāraksta teksts
summa_bez_atlaides = 0.0
kopsumma = 0.0 #galējā summa

while stop == '0':
    ceks
    
    precu_skaits = int(input("Ievadiet preču skaitu:"))
    if precu_skaits < 0: #ja mazak par 0, tad iziet
        exit()
    produkts = input("Ievadiet preces nosaukumu:")
    produkta_cena = round(float(input("Ievadiet cenu par 1 gab. :")),2) #formate 2 sk aiz komata
    
    