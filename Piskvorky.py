"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Pulščák
email: pumi666@atlas.cz
discord: pumi_666
"""
from os import system

oddelovac = "~" * 40
radek = f"     +{'----':^4}+{'----':^4}+{'----':^4}+"
hra, volba, hrac, vstup = True, True, "X", None
pole = ["    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    "]
volna_pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def vitezstvi(kdo):
    print(oddelovac, "\n", "           Gratuluji, hráč ", kdo, "zvítězil!", "\n", oddelovac)
    exit()


# Uvítání
print(oddelovac, "                Vítej ve hře   P I Š K V O R K Y", oddelovac, sep="\n")
print("PRAVIDLA HRY")
input('''2 hráči umisťují střídavě na hrací pole své značky X/O.
Vítězí hráč, kterému se podaří obsadit 3 sousedící pole v řadě, sloupci nebo diagonále.
Značky umisťuješ zadáním čísla volného políčka od 1-9.
Hru spusť libovolnou klávesou, hodně štěstí ;)''')

# Smyčka hry
while hra:

    # Hrací pole
    system("cls")
    print("", radek,
          f"     | {pole[1]:^3} | {pole[2]:^3} | {pole[3]:^3} |", radek,
          f"     | {pole[4]:^3} | {pole[5]:^3} | {pole[6]:^3} |", radek,
          f"     | {pole[7]:^3} | {pole[8]:^3} | {pole[9]:^3} |", radek, sep="\n")

    #   Sloučení políček do řad, sloupců a diagonál
    row1, row2, row3 = pole[1:4], pole[4:7], pole[7:10]
    colmn1 = pole[1] + pole[4] + pole[7]
    colmn2 = pole[2] + pole[5] + pole[8]
    colmn3 = pole[3] + pole[6] + pole[9]
    diag1 = pole[1] + pole[5] + pole[9]
    diag2 = pole[3] + pole[5] + pole[7]

    #   Vyhodnoceni viteze
    if row1.count("X") == 3 or row2.count("X") == 3 or row3.count("X") == 3:
        vitezstvi("X")
    elif colmn1.count("X") == 3 or colmn2.count("X") == 3 or colmn3.count("X") == 3:
        vitezstvi("X")
    elif diag1.count("X") == 3 or diag2.count("X") == 3:
        vitezstvi("X")

    if row1.count("O") == 3 or row2.count("O") == 3 or row3.count("O") == 3:
        vitezstvi("O")
    elif colmn1.count("O") == 3 or colmn2.count("O") == 3 or colmn3.count("O") == 3:
        vitezstvi("O")
    elif diag1.count("O") == 3 or diag2.count("O") == 3:
        vitezstvi("O")

    #  Vyčerpané hrací pole
    if pole.count(" ") == 1:
        print("Všechna pole obsazena, konec hry. REMÍZA", oddelovac, sep="\n")
        exit()

    #    Kontrola vstupu od hráče
    while volba:
        vstup = input(f"Hraje hráč {hrac}  Zadej číslo pole: ")
        if not vstup.isnumeric():
            print(f"{vstup} není číslo, zkus to znova!")
            continue
        elif int(vstup) not in list(range(1, 10)):
            print(f"{vstup} je mimo hrací pole, zkus to znova!")
            continue
        elif int(vstup) not in volna_pole:
            print("Políčko je obsazené! Zkus to znova!")
            continue
        vstup = int(vstup)
        volna_pole.remove(vstup)
        break

    #     Střídání hráčů a přiřazení hráčova symbolu
    pole[int(vstup)] = hrac  # políčko zvoleného indexu se zamění za hráčův X/O
    hrac = ["X", "O"][hrac == "X"]
