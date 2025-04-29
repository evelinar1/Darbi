class Transportlidzeklis: # Klase
    def __init__(self, zimols, modelis, reg_datums, pilna_masa, degvielas_veids): # Konstruktors ar parametriem
        self.zimols = zimols # Lauki
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

    def datu_izvade(self): # Informācijas izvade
        print("Informācija par transportlīdzekli:")
        return f"zīmols: {self.zimols}\nmodelis: {self.modelis}\nreģistrācijas datums: {self.reg_datums}\npilna masa: {self.pilna_masa}\ndegvielas veids: {self.degvielas_veids}"


transportlidzeklis = Transportlidzeklis("Audi","A4","22.10.2019",1800,"BG") # Objekts ar attiecīgiem testa datiem
print( transportlidzeklis.datu_izvade()) # Objektam tiek izsaukta metode