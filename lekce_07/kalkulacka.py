'''
--------------------------------
+ | - | * | / | sum | pow | quit
--------------------------------
'''

def zobraz_nabidku(args):
    spojeni = ' | '.join(args)
    oddelovac = '-' * len(spojeni)
    print(
        oddelovac, 
        spojeni, 
        oddelovac, 
        sep='\n'
        )

# zobraz_nabidku(nabidka)

def umocnovani():
    mocnenec = int(input('Zadej mocnence: '))
    mocnitel = int(input('Zadej mocnitele: '))

    vysledek = mocnenec**mocnitel

    print('Vysledek = ', vysledek)

# umocnovani()

def prumer():
    list_cisel = list()

    while (cislo := input('Zadej cislo: ')) != '=':
        if cislo.isnumeric():
            list_cisel.append(int(cislo))

    vysledek = sum(list_cisel) / len(list_cisel)

    print('Vysledek je : ', vysledek)

# def kalkulacka():
nabidka = ('+', '-', '*', '/', 'pow', 'avg', 'quit')

while True:
    zobraz_nabidku(nabidka)
    
    vyber = input('Vyber si operaci: ')

    if vyber == 'quit':
        print('Na shledanou')
        break

    elif vyber == 'pow':
        umocnovani()

    elif vyber == 'avg':
        prumer()





# kalkulacka()
