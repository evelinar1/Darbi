class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards
        self.parole = parole

    # Izdrukā info par izveidotu lietotāju
    def druka_vardu(self):
        print("Lietotājs", self.vards,"izveidots.")

    def parbauda_paroli(self ,parole):
        # Pārbauda, vai parole sakrīt 
        if self.parole == parole:
            print("Lietotāja", self.vards, "parole ir pareiza.")
        else:
            print("Parole nav pareiza!")

# Klase Darbinieks manto Viesis
# Metode druka_vardu izprintē info par administratoru
class Darbinieks(Viesis):
    def __init__(self, vards, parole):
        super().__init__(vards, parole)

    def druka_vardu(self):
        print("Administrators", self.vards,"izveidots.")

# Testa dati
vards1 = "Valdis"
parole1 = "dators2"

vards2 = "Daina"
parole2 = "monitors2"

# Izveidot objektu klasei Viesis un izsaukt metodes
viesis1 = Viesis(vards1, parole1)
viesis1.druka_vardu()
viesis1.parbauda_paroli(parole1)

viesis2 = Darbinieks(vards2, parole2)
viesis2.druka_vardu()
viesis2.parbauda_paroli(parole2)


