# TODO importy zakladnich knihoven (modulu)
from random import choice, seed
# TODO importy vlastnich modulu
from slova import hadana_slova
from grafika import obesenec


# TODO promenne
zivoty = 7
hra_bezi = True

seed(2)
slovo = choice(hadana_slova)
print(slovo)
tajenka = ['_'] * len(slovo)

# TODO hlavni smycka hry
while hra_bezi and zivoty > 0:

    # TODO zobraz tajenku
    print('Tajenka: ', ' '.join(tajenka))
    
    # TODO input
    hadani = input('Hadej pismeno nebo slovo: ')
    
    # TODO pokud uzivatel uhadl cele slovo
    if hadani == slovo:
        hra_bezi = False
        print('Vyhral jsi')
    
    # TODO pokud uzivatel uhadne pismeno
    elif hadani in slovo and len(hadani) == 1 and hadani not in tajenka:
        for index, pismeno in enumerate(slovo):
            print(index, pismeno)
            
   
    # TODO pokud uzivatel uhadl spatne pismeno
    break
# TODO vypis else po tom, co je while cyklus prerusen

