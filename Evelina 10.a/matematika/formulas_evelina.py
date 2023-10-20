import math
import random
radiuss=float(input("Ievadiet riņķa līnijas rādiusu:"))
print(radiuss)
print("Riņķa līnijas garums:",2*math.pi*radiuss) 
print("Riņķa līnijas laukums:",(math.pow(radiuss,2)))
katetes_garums1=float(input("Ievadiet taisnleņķa trijstūra pirmās katetes garumu:"))
print(katetes_garums1)
katetes_garums2=float(input("Ievadiet taisnleņķa trijstūra otrās katetes garumu:"))
print(katetes_garums2)
print("Taisnleņķa trijstūra hipotenūzas garums:",math.sqrt((math.pow(katetes_garums1,2))+(math.pow(katetes_garums2,2)))) 
#Ģenerē gadījuma skaitli
skaitlis = random.random() #0.1- 1.0 
print("Gadījuma skaitlis no 0 - 1:", skaitlis)