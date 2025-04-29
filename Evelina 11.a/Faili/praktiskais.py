# Ierakstīt teksta failā(no programmas) vārdu, uzvārdu un vecumu
# Dot iespēju izvēlēties: 1 - pievienot datus, 2 - parādīt sakārtotus datus pēc vecuma, 3 - iziet
# Apstrādāt kļūdas
# def pievienot_datus_failam, def sakartot_datus_pec_vecuma, def paradit_sak_datus

name = input("What's your name?: ")
last_name = input("What's your last name?: ")
age = input("What's your age?: ")
with open("info.txt","a",encoding='utf8') as file:
    file.write(f"{name},{last_name},{age}")

#def pievienot_datus_failam():
