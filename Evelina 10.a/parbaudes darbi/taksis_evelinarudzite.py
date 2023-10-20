noligsanas_cena = 1.20
gaidisana = 0.15
izsaukuma_cena = 2.40

pasazieru_sk = int(input("Kāds ir pasažieru skaits?:")) #norādīts pasažieru skaits, ja pārsniedz, programma apstājas
if pasazieru_sk > 4:
    print("Pasažieru skaits nedrīkst būt augstāks par 4.")
elif pasazieru_sk < 4 or pasazieru_sk == 4:
    laiks = int(input("Lūdzu norādiet laiku:"))
    if laiks >= 23 and laiks <= 5: #norādīta cena atkarībā no laika
        tarifs = 0.47
        print("Par katru nobraukto km jāmaksā 0.47 eiro")
    else:
        tarifs = 0.87
        print("Par katru nobraukto km jāmaksā 0.87 eiro")
    stavvieta = input("Vai stāvvietā atrodas kāds taksometrs?(jā/nē):")
    if stavvieta == 'jā':
        print("Jāmaksā tikai nolīgšanas cena.")
    elif stavvieta == 'nē':
        print("Jāmaksā gan nolīgšanas cena, gan izsaukuma cena")
    gaidisanas_laiks = str(input("Vai būs nepieciešams gaidīšanas laiks?(jā/nē):"))
    if gaidisanas_laiks == 'jā':
        ilgums =int(input("Cik ilgs būs gaidīšanas laiks?(min):"))
        attalums = int(input("Cik km garš būs jūsu brauciens?(km):"))
    print("Kopējais pasažiesu skaits:",pasazieru_sk)
    print("Jūsu tarifs ir:",tarifs)
    if stavvieta == 'jā':
        print("Nolīgšanas cena ir:",noligsanas_cena)
    elif stavvieta == 'nē':
        print("Nolīgšanas cena un izsaukšanas cenas summa:",(noligsanas_cena + izsaukuma_cena))
    if gaidisanas_laiks == 'jā':
        print("Summa par gaidīšanas laiku:",(gaidisana*ilgums))





    


                

        


    
    
    
