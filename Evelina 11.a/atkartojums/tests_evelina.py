def noteikt_vertejumu_atzimi(vertejums, atzime):
    if vertejums >= 1 and vertejums <= 10:
        atzime = 1
    elif vertejums >= 11 and vertejums <=20:
        atzime = 2
    elif vertejums >= 21 and vertejums <=30:
        atzime = 3
    elif vertejums >= 31 and vertejums <=40:
        atzime = 4
    elif vertejums >= 41 and vertejums <=53:
        atzime = 5
    elif vertejums >= 54 and vertejums <=66:
        atzime = 6
    elif vertejums >= 67 and vertejums <=76:
        atzime = 7
    elif vertejums >= 77 and vertejums <=86:
        atzime = 8
    elif vertejums >= 87 and vertejums <=94:
        atzime = 9
    elif vertejums >= 95 and vertejums <=100:
        atzime = 10
    return vertejums, atzime
    
def ievadit_rezultatu():
    while True:
        try:
            rezultats = float(input('Testa rezultāts (0-100)'))
            if rezultats >= 0 and rezultats <=100:
                # 0 <= rezultats <=100
                return rezultats
            else:
                print('Ievadiet no 0 - 100')
        except ValueError:
            print('Nederīga ievade.')

def darbiba(): # Programmas galvenā daļa
    while True:
        rezultats = ievadit_rezultatu()
        vertejums, atzime = noteikt_vertejumu_atzimi(rezultats)
        print(f"Rezultāts: {rezultats}% - {vertejums} (atzīme: {atzime})\n")
        
        turpinat = input('Vai ievadīsiet citu rezultātu? (jā/nē): ')
        if turpinat != 'jā':
            print('Programma beigsies!')
            break
    








