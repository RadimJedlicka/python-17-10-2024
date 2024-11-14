mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)

print(nabidka)
print(cara)

destinace = input("CISLO DESTINACE: ")
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
email = input("E-MAIL: ")

print(cara)

cilova_stanice = mesta[int(destinace) - 1] # mesta[int(destinace) - 1
finalni_cena = ceny[int(destinace) - 1]

print(cilova_stanice)
print(finalni_cena, ",-Kč", sep='')

print(cara)

print("Cestujici:", jmeno, prijmeni)
print("Cilova destinace:", cilova_stanice)
print("Cena jizdneho:", finalni_cena, ",-Kč")
print("Jizdenku jsme odeslali na e-mail", email)

