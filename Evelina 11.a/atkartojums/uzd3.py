# Pievienot skaitļus sarakstam
def pievienot_skaitli():
    skaitli = []
    while True:
        try:
            skaitlis = int(input('Ievadiet skaitli (0 - pārtraukt darbu): '))
            if skaitlis == 0:
                break
            skaitli.append(skaitlis)
        except ValueError:
            print('Ievadiet skaitli.')
    print('Saraksts: ', skaitli)

pievienot_skaitli()
