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
    def __init__(self, marka, modelis, gads, akumulatora_ietilp):
        super().__init__(marka, modelis, gads) # Manto atribūtus no bāzes klases 'Masina'
        self.akumulatora_ietilp = akumulatora_ietilp
    # E uzdevums - noklusētā vērtība 100
        self.uzlades_lim = 100
    # F uzdevums - pārrakstīt metodi uzsakt
    def uzsakt(self): # Pārrakstīt metodi, kas veic uzlādes līmeņa pārbaudi
        if self.uzlades_lim >= 20: # Pārbauda vai vērtība atbilst (>=20)
            print(f"{self.marka} {self.modelis} sāk darboties. Akumulators: {self.uzlades_lim}%")
        else:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo akumulators ir pārāk zems: {self.uzlades_lim}%")
    # G uzdevums - info_par_auto pārrakstīšana
    def info_par_auto(self):
        super().info_par_auto()
        print(f"Akumulators: {self.akumulatora_ietilp} kWh.")
# H uzdevums - Izveidots objekts ar pietiekamu uzlādes līmeni
masina2 = Elektro_Auto("Tesla","Model 3",2022,75)
masina2.info_par_auto()
masina2.uzsakt()
# I uzdevums - Izveidots objekts ar nepietiekamu akumulatora līmeni
masina2.uzlades_lim=15
masina2.uzsakt()
print("")

# J uzdevums - Izveidota atvasināta klase 'Degvielas_auto' ar jaunu atribūtu
class Degvielas_auto(Masina):
    def __init__(self, marka, modelis, gads, bakas_tilpums):
        super().__init__(marka, modelis, gads)
        self.bakas_tilpums = bakas_tilpums
        # K uzdevums - Iestatīts degvielas līmeni uz 100
        self.degvielas_lim = 100
    # L uzdevums - pārrakstīt metodi uzsakt
    def uzsakt(self): # Pārrakstīt metodi, kas veic uzlādes līmeņa pārbaudi
        if self.degvielas_lim >= 20: # Pārbauda vai vērtība atbilst (>=20)
            print(f"{self.marka} {self.modelis} sāk darboties. Degvielas līmenis: {self.degvielas_lim}%")
        else:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmenis ir pārāk zems: {self.degvielas_lim}%")
    # M uzdevums - info_par_auto pārrakstīšana
    def info_par_auto(self):
        super().info_par_auto()
        print(f"Bākas tilpums: {self.bakas_tilpums} kWh.")
# N uzdevums - Izveidots objekts ar pietiekamu degvielas līmeni
masina4 = Degvielas_auto("Audi","A7",2022,85)
masina4.info_par_auto()
masina4.uzsakt()
# O uzdevums -Izveidots objekts ar nepietiekamu degvielas līmeni
masina4.degvielas_lim=5      
masina4.uzsakt()
    
