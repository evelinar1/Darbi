class Persona: # Bāzes klase
    def __init__ (self, vards, uzvards, epasts):
        self.vards = vards
        self.uzvards = uzvards
        self.epasts = epasts
    
    def druka_vardu(self):
        print("Šo personu sauc:", self.vards)

class Skolens(Persona): # Atvasinātā klase
    def __init__ (self, vards, uzvards, epasts,vid_atzime=0):
        super().__init__(vards, uzvards, epasts) # Automātiski izsauc bāzes klases konstruktoru
        self.vid_atzime = vid_atzime

    def macities(self):
        self.vid_atzime += 0.1

class Skolotajs(Persona):
    def __init__ (self, vards, uzvards, epasts, macibu_prieksmets):
        super. __init__(vards, uzvards, epasts)
        self.macibu_prieksmets = macibu_prieksmets

    def macit(self):
        print("Mācu:",self.macibu_prieksmets)

# Izveido objektus abām atvasinātajām klasēm

skolens1 = Skolens("Jānis","Bērziņš","janis.berzins@svg.lv",vid_atzime=8.5)
print(skolens1.epasts)

skolens1.macities()
print(skolens1.vid_atzime)

skolotajs1 = Skolotajs("Ilze","Liepiņa","ilze.liepina@svg.lv","matemātika")
print(skolotajs1.vards)
skolotajs1.macit()

