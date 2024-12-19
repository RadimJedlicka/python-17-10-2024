import os

txt_soubor = 'countries_and_cities.txt'

def nacti_txt_soubor(jmeno_souboru):
    try:
        with open(jmeno_souboru, mode='r', encoding='UTF-8') as txt:
            obsah = txt.readlines()
            promenna = None
        
    except FileNotFoundError:
        print(f"SOUBOR: {jmeno_souboru} NENALEZEN!",
              f"ADRESAR: {os.getcwd()}",
              f"OBSAH ADR.: {os.listdir()}", sep="\n")
    
    else:
        print(f'Soubor {jmeno_souboru} je nacten')
        return obsah, promenna
    
    finally:
        print('Funkce ukoncena')

def zformatuj_nazvy():
    for udaj in nacti_txt_soubor(txt_soubor):
        if "quit" in udaj.lower():
            break
        else:
            zeme, mesto = udaj.split(", ")
            print(f"{zeme=:<20} {mesto=}")


zformatuj_nazvy()
    

# print(nacti_txt_soubor(txt_soubor))