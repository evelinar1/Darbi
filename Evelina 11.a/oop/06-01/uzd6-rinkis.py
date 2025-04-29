class Rinkis:
    def __init__(self,radiuss):
        self.radiuss = radiuss

    def iestatit_radiusu(self,radiuss):
        # Ja 0 vai negatīvs, tad uzstāda noklusējumā 1
        if radiuss <=0:
            self.radiuss = 1
        else:
            self.radiuss = radiuss

    def izvadit_radiusu(self):
        return self.radiuss

    def diametrs(self):
        return 2*self.radiuss
        
radiuss = float(input("Ievadiet radiusu: "))
rinkis = Rinkis(radiuss)

print("Riņķa radiuss ir",rinkis.izvadit_radiusu())
print("Riņķa diametrs ir",rinkis.diametrs())