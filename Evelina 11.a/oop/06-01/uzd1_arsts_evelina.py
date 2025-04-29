class Doktorats: # Klase
    def __init__(self):
        self.doktorata_nosaukums = "" # Tukši atribūti, kas glabā lietotāja ievadītās vērtības
        self.pacientu_skaits = ""

    def ievade(self): # Metode, kas ļauj lietotājam ievadīt datus (atribūtu vērtības) un saglabā tās
        self.doktorata_nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        while True: # Ļauj vērtību ievadīt līdz tā ir pareiza
            try:
                self.pacientu_skaits = int(input("Ievadiet doktorāta pacientu skaitu: "))
                break # Ja vērtība ir pareiza, tad programma turpinās
            except ValueError: # Pārbauda vai vērtība ir atbilstoša, ja nav, tad ziņo par kļūdu
                print("Ievadiet skaitli!")

    def datu_izvade(self): # Metode, kas izvada datus
        print(f"Doktorāts {self.doktorata_nosaukums} apkalpo {self.pacientu_skaits} pacientus.")

doktorats = Doktorats() # Objekts
# Objektam izsauktas metodes
doktorats.ievade() 
doktorats.datu_izvade()

                    

