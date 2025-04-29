# Definē klasi Dzivnieks, kas ir saistīta ar kāju skaitu
class Dzivnieks:
    def __init__(self,kaju_skaits=0):
        self.kaju_skaits = kaju_skaits

    @classmethod # Izmanto objektu izveidošanai ar noteiktu kāju skaitu
    def putns(kajas):
        return kajas(2)

    @classmethod 
    def majlops(kajas):
        return kajas(4)

    @classmethod 
    def simtkajis(kajas):
        return kajas(100)

    # Metode, kas izdrukā kāju skaitu
    def izdrukat_kaju_skaitu(self):
        print(self.kaju_skaits)

# Objekts(instance)
odze = Dzivnieks()
zoss = Dzivnieks.putns()
kaza = Dzivnieks.majlops()
simtkajis = Dzivnieks.simtkajis()

odze.izdrukat_kaju_skaitu()
zoss.izdrukat_kaju_skaitu()
kaza.izdrukat_kaju_skaitu()
simtkajis.izdrukat_kaju_skaitu()
