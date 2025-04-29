class Students:
    def __init__ (self, vards, uzvards, vecums, kursa_numurs ):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.kursa_numurs = kursa_numurs

    def datu_ievade(self):
        self.vards = input("Ievadiet studenta vārdu: ")
        self.uzvards = input("Ievadiet studenta uzvārdu: ")
        while True:
            try:
                self.vecums = int(input("Ievadiet studenta vecumu: "))
                if self.vecums < 18:
                    print("Ievadiet atbilstošu vērtību!")
                else:
                    break
            except ValueError:
                print("Ievadiet atbilstošu vērtību!")
        while True:
            try:
                self.kurss = int(input("Ievadiet studenta kursa numuru: "))
                if self.kurss <1 or self.kurss > 4:
                    print("Ievadiet atbilstošu vērtību!")
                else:
                    break
            except ValueError:
                print("Ievadiet atbilstošu vērtību!")

        
    def datu_izvade(self):
        print("---------")
        print(f"Students: {self.vards} {self.uzvards}")
        print(f"Vecums: {self.vecums}")
        print(f"Kurss: {self.kursa_numurs}.kurss")



students= Students()
students.datu_ievade()
students.datu_izvade()

        
