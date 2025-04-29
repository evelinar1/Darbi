def parbaudit_vardu(vards):
    if not vards.isalpha():
        print("Vārds drīkst sastāvēt tikai no burtiem!")
        return False
    return True

def parbaudit_skaitli(skaitlis):
    if int(skaitlis) < 0:
        print("Ievadītais skaitlis nedrīkst būt negatīvs vai 0!")
        return False
    return True
        

def datu_ievade():   
        try:
            while True:
                for vards in range(3):
                    vards = input("Ievadiet savu vardu: ")
                    if vards == 'stop':
                        break
                    if parbaudit_vardu(vards):
                        break
                break
                    
            while True:
                for uzvards in range(3):
                    uzvards = input("Ievadiet savu uzvārdu: ")
                    if uzvards == 'stop':
                        break
                    if parbaudit_vardu(uzvards):
                        break
                break

            while True:
                for vecums in range(3):
                    vecums = (input("Ievadiet savu vecumu:"))
                    if vecums == 'stop':
                        break
                    if parbaudit_skaitli(vecums):
                        break
                break
    
            while True:
                for atzime in range(3):
                    atzime = (input("Ievadiet savu gala atzīmi:"))
                    if atzime == 'stop':
                        break
                    if parbaudit_skaitli(atzime):
                        break
                break

        except ValueError:
            print("Ievadiet atbilstošu vērtību!")
            return vards,uzvards,vecums,atzime

        

'''def saglabat_faila(vards,uzvards,vecums,atzime):
    with open("kontroldarbs.txt","a",encoding='utf8') as file:
        file.write(f"{vards} ,{uzvards} ,{vecums} ,{atzime} ")'''
    


def galvena():
    print("Ievadiet jaunu ierakstu vai ievadiet 'stop' lai pārtrauktu.")
    while True:
        try:
            print("izvēlaties darbību:\n(1) - Ievadīt datus\n(2) - Saglabāt datus failā\n(3) - Parādīt datus sakārtotus pēc gala atzīmes\n(4) - Iziet no programmas")
            izvele = int(input("Jūsu izvēle:"))
            if izvele == 1:
                datu_ievade()
            #elif izvele == 2:
                #saglabat_faila(vards,uzvards,vecums,atzime)
            elif izvele == 4:
                print("Programma beigusies!")
                break
    
        except ValueError:
            print("Ievadiet atbilstošu vērtību!")

galvena()
            



