# TODO importy zakladnich knihoven (modulu)
import random
# TODO importy vlastnich modulu
from grafika import obesenec  
from slova import hadana_slova

# TODO promenne
zivoty = 7
hra_bezi = True
random.seed(2)
slovo = random.choice(hadana_slova)
tajenka = ['_'] * len(slovo)

# TODO hlavni smycka hry
while hra_bezi and zivoty > 0:
    # TODO zobraz tajenku
    print('Tajenka: ', ' '.join(tajenka))
    print(slovo)
    print(obesenec[7 - zivoty])
    # break
    # TODO input
    hadani = input('Hadej pismeno nebo slovo: ')
    
    # TODO pokud uzivatel uhadl cele slovo
    if hadani == slovo:
        print('Vyhral jsi')
        hra_bezi = False

    # TODO pokud uzivatel uhadne pismeno
    elif len(hadani) == 1 and hadani in slovo:
        for poradi, pismeno in enumerate(slovo):
            if pismeno == hadani and tajenka[poradi] == "_":
                tajenka[poradi] = hadani
        hra_bezi = False if '_' not in tajenka else True
        # print(tajenka)
        # print(slovo)
   
    # TODO pokud uzivatel uhadl spatne pismeno
    else:
        print('Zadane pismeno neni v tajence.')
        # zivoty = zivoty - 1
        zivoty -= 1
        print(f'Zbyva ti {zivoty} zivotu.')

# TODO vypis else po tom, co je while cyklus prerusen
else:
    if not hra_bezi:
        print('Vyhral')
    else:
        print('Prohral jsi')
