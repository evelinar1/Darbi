saraksts = [1,2,3,4,5,6,7]
saraksts.append("Cepums")#pievieno saraksta beigās
print(saraksts)

saraksts.pop()#izmet no beigām
print(saraksts)

saraksts.insert(3, 'Hello!')#ievieto 3. no kreisās
print(saraksts)

saraksts.remove(6)#izdzēš norādīto vērtību
print(saraksts)

#funkcijas del pielietojums
tests = [1,2,3,4,5,6,7,8]
del tests[2]#izdzēš vienu elementu
print(tests)

del tests[3:6]
print(tests)#izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2]#no 2-7 elementam dzēš ārā katru otro
print(cipari)