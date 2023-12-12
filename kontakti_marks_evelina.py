kontakti = {
    "Vārds":['Anna','Zane','Jānis','Gustavs'],
    'Nummurs':['309784067806','987956523','468875322','28484843']
}


atbilde = input('Ko vēlaties darīt? \n 1-drukāt kontaktus uz ekrāna \n 2-pievienot kontaktus \n 3-idzēst kontaktus \n 4-iziet \n ')
while atbilde != 4:
    atbilde = input('Ko vēlaties darīt? \n 1-drukāt kontaktus uz ekrāna \n 2-pievienot kontaktus \n 3-idzēst kontaktus \n 4-iziet \n ')
    if atbilde == '1':
        print('jūs uzspiedāt taustiņu 1: jūsu kontakti uz ekrāna: \n',kontakti)
    elif atbilde == '2':
        print('Jūs uzpiedāt taustiņu 2: pievienot jaunu kontaktu: ')
        vards = input('Ievadi vārdu:')
        numurs = input('Ievadi numuru:')
        kontakti['Vārds'].append(vards)
        kontakti['Nummurs'].append(numurs)
    elif atbilde == '3':
        print('Jūs uzpiedāt taustiņu 3: izdzēst kontaktu: ')
        print(kontakti['Vārds'])
        dzest = str(input('Izvēlies kuru no vārdiem vēlies dzēst(raksti 0,1,2,3,4,utt.)'))
        kontakti.pop(dzest)
        print(kontakti)


else: 
    print('Jūs uzpiedāt taustiņu 4: Paldies, ka izmatojāt šo programmu')
    exit()