print("Labdien!")
persona = ['students','personāls']
persona = str(input("Vai jūs esat students vai personāls?: "))
izdevums = ['žurnālu','grāmatu']
izdevums = str(input("Vai jūs vēlaties saņemt žurnālu vai grāmatu?: "))
gramata = ['nav','ir']
gramata = str(input("Vai izdevums ir pieprasīto izdevumu sarakstā?(ir/nav): "))
laika_nenodotas = ['Jā','Nē']
laika_nenodotas = str(input("Vai pie jums atrodas kāds laikā nenodots izdevums?(Jā/Nē): "))

if persona == 'students' and izdevums == 'grāmatu' and gramata == 'nav' and laika_nenodotas == 'Nē':
    print("Grāmatu var saņemt uz 14 dienām.")
if persona == 'students' and izdevums == 'žurnālu' and gramata == 'nav' and laika_nenodotas == 'Nē':
    print("Žurnālu var saņemt uz 7 dienām.")
if persona == 'personāls' and izdevums == 'žurnālu' and gramata == 'nav' and laika_nenodotas == 'Nē':
    print("Žurnālu var saņemt uz 7 dienām.")
if persona == 'personāls' and izdevums == 'grāmatu' and gramata == 'nav' and laika_nenodotas == 'Nē':
    print("Grāmatu var saņemt uz 28 dienām.")
else:
    print("Izdevums netiks izsniegts!")
if persona == 'students' and izdevums == 'grāmatu' and gramata == 'ir' and laika_nenodotas == 'Nē' or persona == 'personāls' and izdevums == 'grāmatu' and gramata == 'ir' and laika_nenodotas == 'Nē':
    print("Grāmatu var saņemt uz 2 dienām.")
if persona == 'students' and izdevums == 'žurnālu' and gramata == 'ir' and laika_nenodotas == 'Nē' or persona == 'personāls' and izdevums == 'žurnālu' and gramata == 'ir' and laika_nenodotas == 'Nē':
    print("Žurnālu var saņemt uz 2 dienām.")
else:
    print("Izdevums netiks izsniegts!")

        

