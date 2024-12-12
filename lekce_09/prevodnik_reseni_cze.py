import os
from pprint import pprint


def spust_prevadeni(soubor: str, slovnik: dict):
    if os.path.isfile(soubor):
        print('Spoustime prevod')
        byty = nacitani_txt_souboru(soubor)
        nova_data = iteruj_pres_vsechna_data(byty, slovnik)
        pprint(nova_data)

    else:
        print('Soubor neexistuje')
    

def nacitani_txt_souboru(soubor: str) -> list:
    with open(soubor, mode='r', encoding='UTF-8') as txt:
        return txt.readlines()
    

def iteruj_pres_vsechna_data(data: list, slovnik: dict) -> list:
    '''
    Pokud v returnu vrátíte list, vypíše se list ve stejném pořadí, v jakém se iteroval.
    Pokud v returnu vrátíte set ( pomocí {}), hodnoty se seřadí sestupně
    '''
    # for detail in data:
    #     novy_detail = prepis_novy_typ_bytu(detail, slovnik)

    return [
        prepis_novy_typ_bytu(detail, slovnik) 
        for detail in data
    ]


def prepis_novy_typ_bytu(detail: str, slovnik: dict) -> str:
    '''
    Pozor na doplňování hodnot ze slovníků pomocí klíču (metoda .get):
    Pokud klíč nebude nalezen, program skončí chybou (jako zde v případě 
    předposledního řádku našeho souboru, kde je "byt0008".)
    Můžeme to ale pohlídat pomocí druhého argumentu metody .get,
    kde zapíšeme string, který se doplní v případě, že klíč nebyl nalezen.
    '''
    dispozice, *zbytek = detail.split(',', maxsplit=1)
    novy_zapis = slovnik.get(dispozice, 'Neznama pozice')
    return ', '.join((novy_zapis, ', '.join(zbytek)))


def prevod_bytu():

    abs_cesta = f'{os.getcwd()}{os.sep}solution{os.sep}vstupni_data.txt'

    prevodni_vzor = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
    }

    spust_prevadeni(abs_cesta, prevodni_vzor)


if __name__ == '__main__':
    prevod_bytu()
    
