import os
from random import choice, seed

# from slova import hadana_slova
# from grafika import obesenec
hadana_slova = ['dva', 'hudba', 'vecernicek']

zivoty = 7
hra_bezi = True
# seed(2) # slovo je 'vojna'
# slovo = choice(hadana_slova)
# tajenka = ['_'] * len(slovo)

#### Definovane funkce #########################################
def tajne_slovo(list_tajnych_slov):
    return choice(list_tajnych_slov)

slovo = tajne_slovo(hadana_slova)
print(slovo)

def vytvor_tajenku(vstupni_slovo):
    return ['_'] * len(vstupni_slovo)

tajenka = vytvor_tajenku(slovo)
print(tajenka)

def zobraz_stav_hry(list_s_tajenkou, pocet_zivotu):
    # os.system("cls") # mac, linux "clear"
    print(f"Tajenka: {''.join(list_s_tajenkou)}")
    print(f"Zbyvajici pocet zivotu: {pocet_zivotu}")

test = zobraz_stav_hry(tajenka, zivoty)
print(test)

def co_hada_uzivatel():
    return input('Hadej pismeno/cele slovo: ')

test = co_hada_uzivatel()
print(test)




#### Beh programu ##############################################

while hra_bezi and zivoty > 0:
    os.system("cls")
    print(f"Tajenka: {''.join(tajenka)}")
    print(f"Zbyvajici pocet zivotu: {zivoty}")
    hadani = input('Hadej pismeno/cele slovo: ')

    if hadani == slovo:
        hra_bezi = False
    elif hadani in slovo and len(hadani) == 1:
        for index, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[index] = hadani
        print('Uhodl jsi spravne pismeno!')
        if '_' not in tajenka:
            hra_bezi = False
    else:
        print('Pismeno neni v tajence, hadej znova!')
        zivoty -= 1
else:
    if hra_bezi == False:
        print('Vyhral jsi!')
    else:
        print(f'Prohral jsi, tajenka byla "{slovo}"')