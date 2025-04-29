from abc import ABC, abstractmethod
class SkolasDarbinieks(ABC):
    def __init__(self,vards,uzvards):
        self.vards = vards
        self.uzvards= uzvards
    @abstractmethod # Izveidota abstrakta klase
    def apraksts(self):
        pass

class Skolotajs(SkolasDarbinieks): # Mantota klase
    def __init__(self,vards,uzvards,prieksmets):
        super().__init__(vards,uzvards)
        self.prieksmets = prieksmets
    def apraksts(self): # Realizē metodi apraksts
        return(f"Skolotājs {self.vards} {self.uzvards} pasniedz {self.prieksmets}.")

class Skolens(SkolasDarbinieks):
    def __init__(self,vards,uzvards,vid_atzime):
        super().__init__(vards,uzvards)
        self.vid_atzime = vid_atzime
    def apraksts(self):
        return(f"Skolēns {self.vards} {self.uzvards}, vidējā atzīme: {self.vid_atzime}.")

class Direktors(SkolasDarbinieks):
    def __init__(self,vards,uzvards,stradasanas_gadi):
        super().__init__(vards,uzvards)
        self.stradasanas_gadi = stradasanas_gadi
    def apraksts(self):
        return(f"Direktors, {self.vards} {self.uzvards}, skolā strādā {self.stradasanas_gadi} gadus.")

class Lietvedis(SkolasDarbinieks):
    def __init__(self,vards,uzvards,darba_stundas):
        super().__init__(vards,uzvards)
        self.darba_stundas = darba_stundas
    def apraksts(self):
        return(f"Lietvedis, {self.vards} {self.uzvards}, dienā strādā {self.darba_stundas} stundas.")

# Saraksts ar objektiem un to argumentiem
darbinieki = [ 
    Skolotajs("Igors","Laimnesis","Fizika"),
    Skolens("Ieva","Strautiņa",7),
    Direktors("Ulģis","Akmentiņš",4),
    Lietvedis("Pēteris","Drudzis",8)
]
# Parāda informāciju uz ekrāna
for darbinieks in darbinieki:
    print(darbinieks.apraksts())

# Saglabā informāciju teksta failā
with open ("darbinieki.txt","w",encoding="utf8") as file:
    for darbinieks in darbinieki:
        file.write(darbinieks.apraksts()+"\n")
