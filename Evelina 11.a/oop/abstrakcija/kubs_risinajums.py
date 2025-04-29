class Kubs:
    def __init__(self,malas_garums,krasa): 
            if malas_garums >=2 and malas_garums <=10: 
                self.malas_garums = malas_garums
            else:
                print("Malas garums neatbilst nosacījumiem!")
                self.malas_garums = 2 
            self.krasa = krasa

    def aprekinat_tilpumu(self):
        tilpums = self.malas_garums**3 # Kāpina kubā
        return tilpums

class Bloks(Kubs):
    def __init__(self, kubu_skaits,krasa,malas_garums,forma):
        super().__init__(malas_garums,krasa)
        if kubu_skaits >=1 and kubu_skaits <=4: 
            self.kubu_skaits = kubu_skaits
        else:
            print("Nepareiza kubu skaita vērtība!")
            self.kubu_skaits = 1
        self.nosaukums = self.krasa+str(self.kubu_skaits) 
        formas_vertibas = [11,12,13,14,22]
        if forma not in formas_vertibas:
            print("Forma neatbilst nosacījumiem!")
            self.derigums = 'nederīgs 0'
        else:
            self.derigums = 'derigs 1'
            
    def tilpums(self):
        kuba_tilpums = self.malas_garums**3
        bloka_tilpums = kuba_tilpums*self.kubu_skaits
        return bloka_tilpums

    def mainit_formu(self,jauna_forma):
        formas_vertibas = [11,12,13,14,22]
        if jauna_forma not in formas_vertibas:
            print("Forma neatbilst nosacījumiem!")
            self.derigums = 'nederīgs 0'
        else:
            self.derigums = 'derigs 1'

# Objekti
print("Dati par kubg objektu:")
kubg = Kubs(10,"Zaļa") 
print('Kubg krāsa un tilpums: ',kubg.krasa, kubg.aprekinat_tilpumu())
print('Kubg malas garums: ',kubg.malas_garums,'\n***')

print("Dati par kubg objektu:")
kubr = Kubs(1,"Sarkana") 
print('Kubr krāsa un tilpums: ',kubr.krasa, kubg.aprekinat_tilpumu())
print('Kubr malas garums: ',kubr.malas_garums,'\n***')

print("Oranžš objekts")
orange3 = Bloks(5,"oranza",3,13)
print(orange3.nosaukums,orange3.tilpums(),orange3.derigums,'\n***')

print("Zils objekts")
blue5 = Bloks(7,"zila",5,23)
print(blue5.nosaukums,blue5.derigums,'\n***')

print("Mainīta forma")
blue5.mainit_formu(12)
print(blue5.nosaukums,blue5.malas_garums,blue5.derigums,'\n***')