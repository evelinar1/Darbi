# Izveidot klasi BankasKonts
# Ielikt 2 atribūtus - klienta vārds un atlikums
# Klasē ir 2 metodes - iemaksat(summa) - palielinās konta atlikumu ar norādīto summu
# Metode iznemt(summa) - samazina konta atlikumu par norādīto summu, ja pietiek līdzekļu
# Objekti - klientam Laura sākumā ir 100 eiro | iemaksā 50, pārbauda atlikumu
# Izņemt 30, pēc tam mēģina izņemt 200, lai notestētu gadījumu, kad nav līdzekļu

class BankasKonts:
    def __init__(self,vards,atlikums): # Konstruktors ar 2 parametriem
        self.vards = vards # Lauki
        self.atlikums = atlikums

    # Metode iemaksai
    def iemaksat(self,summa):
        self.atlikums+=summa # Palielina atlikumu
        return f"Iemaksāti {summa} Eur. Jaunais atlikums: {self.atlikums} EUR."

    def iznemt(self,summa):
        # Pārbauda vai pietiek līdzekļu
        if summa > self.atlikums:
            return "Nav pietiekami daudz līdzekļu."  
        self.atlikums-=summa # Samazina konta atlikumu
        return f"izņemti {summa} EUR. Jaunais atlikums: {self.atlikums} EUR."


konts = BankasKonts("Laura",100)

print(konts.iemaksat(50))
print(konts.iznemt(30))
print(konts.iznemt(200))


        
