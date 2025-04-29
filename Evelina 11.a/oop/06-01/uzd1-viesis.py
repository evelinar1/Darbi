# Klase Viesis ar konstruktoru(inicializatoru)

class Viesis:
    def __init__(self,vards,parole):
        self.vards = vards # Izveido lauku
        self.parole = parole

    def druka_vardu(self):
        print("Lietotājs", self.vards, "izveidots.")

    def parbauda_paroli(self,parole):
        if self.parole == parole:
            print("Lietotāja", self.vards, "parole ir pareiza.")

vards = "Valdis"
parole = "12345"

# Izveido objektu

viesis1 = Viesis(vards,parole)
# Objektam izsauc metodes
viesis1.druka_vardu()
viesis1.parbauda_paroli(parole)

