# Uz ekrāna izdrukāt visus nepāra skaitļus no lietotāja ievadītā diapazona
sakums = int(input('Sākums: '))
beigas = int(input('Beigas: '))

for skaitlis in range(sakums,beigas+1):
    if skaitlis%2 !=0:
        print(skaitlis)

