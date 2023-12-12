#piemērs sarakstam ar dažādiem datu tipiem
mixed_list = ['suns',7.25,8,True]
print(mixed_list[2])

#apgriezt skaitļu sarakstu
skaitli = [1,2,4,5,6,7,3,4,7,8,9,7]
apgriezts = list(reversed(skaitli))
print(apgriezts)

#filtrēt tikai pāris skaitļus
para_skaitli = [num for num in skaitli if num%2 == 0]
print(para_skaitli)

#iegūst saraksta garumu

videjais = sum(skaitli)/len(skaitli)
print(f"Vidējais skaitlis: {videjais}")

#atrast lielāko un mazāko skaitli, parādīt uz ekrāna

mazakais_sk = min(skaitli)
print(f"Mazākais skaitlis: {mazakais_sk}")
lielakais_sk = max(skaitli)
print(f"Lielākais skaitlis: {lielakais_sk}")

augli = ['abols','ananass','mango','citrons','bumbieri']
#atrast vārdus, kas sākas ar konkrētu burtu
varda_sakums = [vards for vards in augli if vards.startswith('a')]
print(f"Vārdi, kas sākas ar 'a':{varda_sakums}")


