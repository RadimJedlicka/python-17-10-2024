import sys

# Načtení seznamu z nákupního listu
with open("shopping_list.txt", "r") as f:
    shopping_list = f.read().splitlines()

print("Původní nákupní seznam:")
print(shopping_list)

# Přidání nových položek na konec seznamu
if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        shopping_list.append(item)

# Vypsání upraveného seznamu
print("Upravený nákupní seznam:")
print(shopping_list)

# Uložení seznamu zpět do souboru
with open("shopping_list.txt", "w") as f:
    for item in shopping_list:
        f.write(item + "\n")
