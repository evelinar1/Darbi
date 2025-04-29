import csv
from datetime import datetime

class Rekins:
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers # Platums, garums, augstums
        self.materials = materials
        self.laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.darba_samaksa = 15
        self.PVN = 21
        #self.summa = 0 Aprēķinās vēlāk, izsaucot aprekins()
        self.summa = self.aprekins() # Aprēķinās pēc objekta izveidošanas, pamatojoties uz citiem parametriem

    def aprekins(self): # Self atsaucas uz pašreizējo objektu, tātad uz visiem objektiem, kas ir pieejami
        # "izpakot" izmērus
        platums, garums, augstums = self.izmers
        veltijums_garums = len(self.veltijums)
        produkta_cena = (veltijums_garums*1.20)+(platums/100)*(garums/100)*(augstums/100)/3*self.materials
        PVN_summa = (produkta_cena+self.darba_samaksa)*self.PVN/100
        rekina_summa = (produkta_cena+self.darba_samaksa)+PVN_summa
        return round(rekina_summa,2)

    def izdruka(self):
        print("\nRĒĶINS")
        print(f"Izveidošanas laiks: {self.laiks}")
        print(f"Klients: {self.klients}")
        print(f"Veltījums: {self.veltijums}")
        print(f"Izmērs (mm): platums = {self.izmers[0]}, garums = {self.izmers[1]}, augstums = {self.izmers[2]}")
        print(f"Kokmateriāla cena (EUR/m^2): {self.materials}")
        print(f"Darba samaksa: {self.darba_samaksa} EUR")
        print(f"PVN: {self.PVN}%")
        print(f"Kopējā summa: {self.summa} EUR")

    def saglabat(self):
        datnes_nosaukums = f"rekins_{self.klients}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open (datnes_nosaukums,'w',newline='',encoding='utf-8') as fails:
            rakstitajs = csv.writer(fails)
            rakstitajs.writerow(["Izveidošanas laiks","Klients","Veltījums","Izmērs","Cena (EUR/m^2)","Darba samaksa","PVN (%)","Summa (EUR)"])
            rakstitajs.writerow([self.laiks,self.klients,self.veltijums,
                                f"{self.izmers[0]}X{self.izmers[1]}X{self.izmers[2]}",
                                self.materials,self.darba_samaksa,self.PVN,self.summa])
            print(f"Rēķins saglabāts failā: {datnes_nosaukums}")

klients = input("Ievadiet klienta vārdu: ")
veltijums = input("Ievadiet veltījuma tekstu: ")
platums = int(input("Ievadiet lādītes platumu (mm): "))
garums = int(input("Ievadiet lādītes garumu (mm): "))
augstums = int(input("Ievadiet lādītes augstumu (mm): "))
materials = float(input("Ievadiet materiāla cenu (EUR/m^2): "))

# Jauna rēķina objekta izveidošana
rekins = Rekins(klients,veltijums,[platums,garums,augstums],materials)
# Saglabāt un izdrukāt rēķinu
rekins.saglabat()
rekins.izdruka()
#rekins.aprekins() - # Ja pie laukiem liek, ka summa = 0 



