import os

def spust_prevadeni(soubor):
    print(soubor)
    if os.path.isfile(soubor):
        print('Cteme soubor')
        byty = nacitani_txt_souboru(soubor)
        iteruj_vsechna_data(byty)

    else:
        print('soubor nenalezen')

def iteruj_vsechna_data(data):
    for radek in data:
        print(radek.split(',', maxsplit=1)[0])

def nacitani_txt_souboru(txt_soubor):
    with open(txt_soubor, mode='r', encoding='UTF-8') as txt:
        return txt.readlines()

def prevod_typu():

    abs_cesta = f'{os.getcwd()}{os.sep}lekce_09{os.sep}solution{os.sep}vstupni_data.txt'

    prevodni_vzor = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
    }

    spust_prevadeni(abs_cesta)


prevod_typu()
