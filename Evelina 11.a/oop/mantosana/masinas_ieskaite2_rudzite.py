# A uzdevums - Izveidota bāzes klase ar atribūtiem
class Masina:
    def __init__(self, marka, modelis, gads):
        self.marka = marka # Atribūti
        self.modelis = modelis
        self.gads = gads
# B uzdevums - Izveidotas metodes
    def uzsakt(self): # Metode parāda, ka mašīna sāk darboties
        print(f"{self.marka} {self.modelis} sāk darboties.")

    def apstādināt(self): # Metode parāda, ka mašīna apstājas
        print(f"{self.marka} {self.modelis} ir apstādināta.")

    def info_par_auto(self): # Metode parāda informāciju par automašīnu
        print(f"Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads}")
# C uzdevums - Izveidots objekts klasei 'Masina'
masina1 = Masina("Toyota","Corolla",2010)
masina1.info_par_auto()
masina1.uzsakt()
masina1.apstādināt()
print("")

# D uzdevums - Izveidota atvasināta klase 'Elektro_auto' ar jaunu atribūtu
class Elektro_Auto(Masina):
# E uzdevums - Iestatīts akumulatora uzlādes līmenis uz 100 
    def __init__(self, marka, modelis, gads, akumulatora_ietilp=100):
        super().__init__(marka, modelis, gads) # Manto atribūtus no bāzes klases 'Masina'
        self.akumulatora_ietilp = akumulatora_ietilp # Pievienots jauns atribūts   
# F uzdevums - Pārrakstīta metode 'uzsakt()' lai pārbaudītu vai uzlādes līmenis ir >= 20
    def uzsakt(self):
        if self.akumulatora_ietilp >= 20: # Pārbauda vai vērtība atbilst (>=20)
            print(f"{self.marka} {self.modelis} sāk darboties. Akumulators: {self.akumulatora_ietilp}%")
        elif self.akumulatora_ietilp < 20:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo akumulators ir pārāk zems: {self.akumulatora_ietilp}%")
# G uzdevums - Pārraksta metodi 'info_par_auto()', parāda akumulatora ietilpību kWh
    def info_par_auto(self):
        print(f"Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads}\nAkumulators: {self.akumulatora_ietilp} kWh")
# H uzdevums - Izveidots objekts ar pietiekamu uzlādes līmeni
masina2 = Elektro_Auto("Tesla","Model 3",2022,75)
masina2.info_par_auto()
masina2.uzsakt()
# I uzdevums - Izveidots objekts ar nepietiekamu akumulatora līmeni
masina3 = Elektro_Auto("Tesla","Model 3",2022,15)
masina3.uzsakt()
print("")

# J uzdevums - Izveidota atvasināta klase 'Degvielas_auto' ar jaunu atribūtu
class Degvielas_auto(Masina):
# K uzdevums - Iestatīts degvielas līmeni uz 100
    def __init__(self, marka, modelis, gads, bakas_tilpums=100):
        super().__init__(marka, modelis, gads)
        self.bakas_tilpums = bakas_tilpums
# K uzdevums - Iestatīts degvielas līmenis uz 100
        
# L uzdevums - Pārrakstīta metode 'uzsakt()' tā, lai pārbaudītu vai degvielas līmenis ir >=10
    def uzsakt(self):
        if self.bakas_tilpums >= 10:
            print(f"{self.marka} {self.modelis} sāk darboties. Degvielas līmenis: {self.bakas_tilpums}%")
        elif self.bakas_tilpums < 10:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmenis ir pārāk zems: {self.bakas_tilpums}%")
# M uzdevums - Pārraksta metodi 'info_par_auto()', parāda bākas tilpumu
    def info_par_auto(self):
        print(f"Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads}\nBākas tilpums: {self.bakas_tilpums} litri")
# N uzdevums - Izveidots objekts ar pietiekamu degvielas līmeni
masina4 = Degvielas_auto("Audi","A7",2022,85)
masina4.info_par_auto()
masina4.uzsakt()
# O uzdevums -Izveidots objekts ar nepietiekamu degvielas līmeni
masina5 = Degvielas_auto("Audi","A7",2022,5)      
masina5.uzsakt()

        

        

