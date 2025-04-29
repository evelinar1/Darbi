# Bāzes klases Persona ar laukiem vārds, vecums un metodi, kas šos datus izdrukā
class Persona:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
    def dati(self):
        print("Vārds:",self.vards,"\nVecums:",self.vecums)
# Atvasinātā klase students, kas manto abus divus laukus un pievieno specifisko lauku "kurss"
class Students(Persona):
    def __init__(self, vards, vecums,kurss):
        super().__init__(vards,vecums)
        self.kurss = kurss
    # metodes pārrakstīšana
    def dati(self):
        super().dati()
        print("Kurss:",self.kurss)
# Izveidot katrai klasei vienu objektu

students1 = Persona("Alnis",20)
students1.dati()

students2 = Students("Sandra",19,2)
students2.dati()

super(Students, students2).dati()