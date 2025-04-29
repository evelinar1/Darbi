'''# Saglabāt datus sarakstā
names = []
for i in range(3):
    names.append(input("What's your name?"))
# Atgriež sakārtotus
for name in sorted(names):
    print(f"Hello,{name}")'''

'''# Informāciju no konsoles ieraksta failā
name = input("What's your name?: ")
file = open("names.txt","a",encoding='utf8') # w izveido un ieraksta datus
# a režīmā izveido failu, bet informāciju pievieno klāt (nevis aizvieto)
file.write(f"{name}\n")
file.close() # Ja izmanto 'file = open', tad jāaizver failu ciet'''

# Lieto context manager - fails nav jāaizver
'''name = input("What's your name?: ")
with open("names.txt","a",encoding='utf8') as file:
    file.write(f"{name}\n")'''

'''# Nolasīt informāciju no faila
with open("names.txt",encoding='utf8') as file:
    for line in file:
        print("Hello,",line.rstrip())'''

# Atgriezt sakārtotus datus no faila
names = []
with open ("names.txt",encoding='utf8') as file:
    for line in file:
        names.append(line.rstrip())
# Atgriež sakārtotus vārdus
for name in sorted(names):
    print(f"Hello,{name}")



