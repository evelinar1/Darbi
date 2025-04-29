from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self,vards,epasts):
        self.vards = vards
        self.epasts = epasts

class Vestule(Persona):
    def __init__(self,nosutitajs,sanemejs,saturs):
        self.nosutitajs = nosutitajs
        self.sanemejs = sanemejs
        self.saturs = saturs
        
class VestuleSuta(ABC):
    def __init__(self,vestule):
        self.vestule = vestule
    @abstractmethod
    def sutit_vestuli():
        pass
    @abstractmethod
    def sanemt_vestuli():
        pass

class Pastnieks(VestuleSuta):
    def __init__(self,vestule):
        super().__init__(vestule)
    def sutit_vestuli(self,vestule):
        print("Vēstule nosūtīta ar pastnieka palīdzību")
        

