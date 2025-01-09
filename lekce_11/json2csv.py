import os
import json
import csv
from pprint import pprint

# relativni cesta k souboru
rel_cesta = 'solution/'

# potrebne klice
zadouci_klice = ("first_name", "last_name", "email")

# fce json_to_csv
def json_to_csv():
    jsony = najdi_jsons(rel_cesta)
    vsechna_data = nacti_jsony(rel_cesta, jsony)
    upravena_data = uprav_data(vsechna_data)
    
    return upravena_data

# funkce, ktera najde vsechny json soubory
def najdi_jsons(relativni_cesta):
    list_souboru = []

    for jmeno_souboru in os.listdir(relativni_cesta):
        if jmeno_souboru.endswith('.json') and '_' in jmeno_souboru:
            list_souboru.append(jmeno_souboru)
    
    return list_souboru

# funkce, ktera nacte obsah nalezenych jsonu
def nacti_jsony(rel_cesta, jsony):
    json_data = []

    for jmeno_souboru in jsony:
        with open(rel_cesta + jmeno_souboru, 'r') as soubor:
            data = json.load(soubor)
            json_data.append(data)
    
    return json_data

# funkce, ktera upravi obsah souboru
def uprav_data(data):
    upravena_data = []

    for radek in data:
        # Ensure radek is a dictionary
        if isinstance(radek, dict):
            novy_radek = {klic: radek.get(klic) for klic in zadouci_klice}
        else:
            print("Error: radek is not a dictionary")
        upravena_data.append(novy_radek)
    
    return upravena_data


test = json_to_csv()
print(test)

# funkce, ktera ulozi soubory do csv na lokal

# zabaleni do hlavni funkce