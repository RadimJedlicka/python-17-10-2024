# TODO: vypsani nabidky

def zobraz_nabidku():
    nabidka = ['+', '-', '*', '/', 'pow', 'avg', 'quit']
    spojeni = ' | '.join(nabidka)
    oddelovac = '-' * len(spojeni)
    print(oddelovac, spojeni, oddelovac, sep='\n')


# TODO: prumer
def vypocti_prumer():
    list_cisel = []

    while (cislo := input('Zadej cislo: ')) != '=':
        if cislo.isnumeric():
            list_cisel.append(int(cislo))

    vysledek = sum(list_cisel) / len(list_cisel)
    print(vysledek)
# vypocti_prumer()


# TODO: umocnovani
def umocnovani():
    mocnenec = int(input('Zadej mocnence: '))
    mocnitel = int(input('Zadej mocnitele: '))

    vysledek = mocnenec**mocnitel

    print(vysledek)

# umocnovani()

# TODO hlavni funkce Kalkulacka
def kalkulacka():
    while True:

        zobraz_nabidku()

        vyber = input('Vyber funkci: ')

        if vyber == 'quit':
            break
        elif vyber == 'avg':
            vypocti_prumer()
        elif vyber == 'pow':
            umocnovani()


kalkulacka()


# TODO: zakladni matematicke operace


# TODO: sinus
# TODO: cosinus