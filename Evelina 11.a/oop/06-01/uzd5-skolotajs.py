class Skolotajs: # Izveido klasi
    # Konstruktors
    def __init__(self,vards,prieksmets):
        self.vards = vards # Lauki
        self.prieksmets = prieksmets
    # Metodes
    def iepazistinat_ar_sevi(self):
        print(f"Sveiki, mani sauc {self.vards}!")

    def izlikt_vertejumu(self,atzime):
        if atzime < 4: 
            return f"priekšmets {self.prieksmets} nav nokārtots!"
        elif atzime > 4:
            return f"Priekšmets {self.prieksmets} ir nokārtots!"

# Instancēšana / objektu izveidošana
skolotajs1 = Skolotajs("Rinalds","matemātika")
skolotajs2 = Skolotajs("Sandra","bioloģija")

skolotajs1.iepazistinat_ar_sevi() # Izsauc metodi objektam
print(skolotajs1.izlikt_vertejumu(6))
skolotajs2.iepazistinat_ar_sevi()
print(skolotajs2.izlikt_vertejumu(2))

