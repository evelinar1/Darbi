from abc import ABC, abstractmethod

# Vispārīga datu struktūra, kas nepieciešama visām grāmatām
class Gramata(ABC): # Abstraktā klase ar metodi gramatas_dati
    @abstractmethod
    def gramatas_dati(self):
        pass

# Izveidot divas apakšklases, kur katra metodi (gramatas_dati) realizē citādāk
class Hobits(Gramata):
    def gramatas_dati(self):
        print("Hobits, 654 lpp")

class DaVinciKods(Gramata):
    def gramatas_dati(self):
        print("Da Vinči koda autors ir Dens Brauns.")

gramata1 = Hobits()
gramata1.gramatas_dati()

gramata2 = DaVinciKods()
gramata2.gramatas_dati()