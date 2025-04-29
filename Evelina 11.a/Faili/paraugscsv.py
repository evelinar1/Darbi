import csv
# Izveidos csv failu un ļaus rakstīt datus
'''with open("students0.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","House"]) # Pievieno kolonnu nosaukumus
    # Iegūst datus no lietotāja
    while True:
        name = input("Enter name and house (type 'ok' to finish):")
        if name.lower() == 'ok':
            break
        student_house = input(f"Enter {name}'s house:")
        writer.writerow([name,student_house])
        print(f"{name} has been added.\n")'''

# Nolasīt informāciju no csv faila, sakārtot
students = []
with open("students0.csv",encoding='utf8') as file:
    for line in file: # Cikla mainīgais katrā iterācijā iegūst rindiņas saturu kā txt virkni
        name,house = line.rstrip().split(",") # Noņem liekos simbolus rinas beigās, ar split sadala tekstu
        students.append(f"{name} is in {house}.")
for student in sorted(students):
    print(student)





