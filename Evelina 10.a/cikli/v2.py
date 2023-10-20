'''atbilde = 'j'
while atbilde == 'j':
    print("Nekusties!")
    atbilde =input("Vai briesmonis ir draudzīgs?(j/n):")
else:
    print("Bēdz prom?")'''

#pārbaudīt vai lietotājs prot reizināt ar 7
#programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi
reiz = 7
for i in range(1,13): #cikla mainīgais no 1 - 12
    print("Cik ir",i,"x",reiz,"?")
    minejums = input()
    if minejums == 'stop':
        break #pārtrauc programmu
    if minejums == 'izlaist':
        print("Tiek izlaizts")
        continue #izlaiž 1 jautājumu un turpina tālāk
    atbilde = i * reiz
    if int(minejums) == atbilde:
        print("Pareizi!")
    else:
        print("Nē, tas ir,", atbilde)

