# 1. Uzdevums
class Kubs:
    def __init__(self,malas_garums,krasa,nosaukums): # 1.1. Konstruktors, kurš veic datu kontroli
            if malas_garums >=2 and malas_garums <=10: # Tiek pārbaudīts, vai argumenti atbilst prasībām (2-10cm)
                self.malas_garums = malas_garums
            else:
                print("Malas garums neatbilst nosacījumiem!")
                self.malas_garums = 2 # Ja vērtība neatbilst nosacījumiem, tiek iestatīta mazākā vērtība 
            self.krasa = krasa
            self.nosaukums = nosaukums

    def aprekinat_tilpumu(self):
        tilpums = self.malas_garums*self.malas_garums*self.malas_garums # Kuba tilpums ( mala^3 )
        print(f"{self.nosaukums} krāsa un tilpums: {self.krasa} {tilpums}\n{self.nosaukums} malas garums: {self.malas_garums}")

# 1.2. Klases kubs objekts 'kubg'
print("Dati par kubg objektu:")
kubg = Kubs(10,"Zaļa","kubg") # 1.4. Uz ekrāna tiek parādīta kubg krāsa un tilpums
kubg.aprekinat_tilpumu() # 1.5. Uz ekrāna parāda kubg malas garumu
print('***')

# 1.3. Klases kubs objekts 'kubr'
print("Dati par kubr objektu:")
kubr = Kubs(1,"Sarkana","kubr") # 1.6. kubr krāsa un tilpums
kubr.aprekinat_tilpumu() # 1.7. kubr malas garumu
print('***')

# 2. Uzdevums
class Bloks(Kubs):
    def __init__(self, kubu_skaits,forma,malas_garums,krasa,nosaukums,platums,augstums):
        super().__init__(malas_garums,krasa,nosaukums)
        self.platums = platums
        self.augstums = augstums
        if kubu_skaits >=1 and kubu_skaits <=4: # 2.1. Veic pārbaudi, lai nodrošinātu, ka vērtība atbilst prasībām (1-4)
            self.kubu_skaits = kubu_skaits
        else:
            print("Nepareiza kubu skaita vērtība!")
            self.kubu_skaits = 1 # 2.1.1 Ja vērtība neatbilst iestata noklusētu vērtību 1
        self.nosaukums = nosaukums
        if forma   in [11,12,13,14,22]: # 2.1.2 Ja 'forma' vērtība atbilst iestata derīguma vērtību uz 1, ja neatbilst uz 0
            self.forma = self.augstums*self.platums
            self.derigums = ("derigs 1") 
            
        else:
            print("Forma neatbilst nosacījumiem!")
            self.derigums = ("nederīgs 0") 
            self.augstums = 0
            self.platums = 0
            self.forma = self.augstums * self.platums
            
    def tilpums(self):
        bloka_tilpums = self.malas_garums*self.malas_garums*self.malas_garums*self.forma # Tiek aprēķināts tilpums blokam ( mala^3 * augstums * platums)
        print(f"{self.nosaukums} {bloka_tilpums} {self.derigums}")

# 2.2 Objekts klasei bloks
print("Oranžs objekts:")
kubo = Bloks(3,13,5,"Oranžs","oranža3",1,3)
kubo.tilpums() # 2.3 Izvadīta informācija
print('***')
# 2.4 Objekts klasei bloks ar neatbilstošām vērtībām
print("Zils objekts:")
kubz = Bloks(5,23,7,"Zils","zila1",0,0)
kubz.tilpums() # 2.5 Izvadīta informācija
print('***')
# 2.6 Objekts ar nomainītām vērtībām
print("Mainīta forma:")
kubz = Bloks(1,12,7,"Zils","zila1",1,2)
kubz.tilpums() # 2.7 Izvadīta informācija
        