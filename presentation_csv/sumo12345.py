import csv
# Dane zawodników sumo
sumo_zawodnicy = [
    {"Imie": "Hakuho", "Nazwisko": "Sho", "Kraj": "Mongolia", "Waga": 154, "Wzrost": 192},
    {"Imie": "Kisenosato", "Nazwisko": "Yutaka", "Kraj": "Japonia", "Waga": 178, "Wzrost": 186},
    {"Imie": "Asanoyama", "Nazwisko": "Hideki", "Kraj": "Japonia", "Waga": 167, "Wzrost": 188},
    {"Imie": "Terunofuji", "Nazwisko": "Haruo", "Kraj": "Mongolia", "Waga": 177, "Wzrost": 191},
    {"Imie": "Enho", "Nazwisko": "Akira", "Kraj": "Japonia", "Waga": 98, "Wzrost": 169},
]


nazwa_pliku = r'C:\Users\Ania\Desktop\zawodnicy_sumo_stoworzne.csv'

# Otwarcie pliku do zapisu
with open(nazwa_pliku, mode='w', newline='') as file:
    csv_writer = csv.writer(file)

    # Zapisanie nagłówka
    lista = ["Imie", "Nazwisko", "Kraj", "Waga (kg)", "Wzrost (cm)"]
    csv_writer.writerow(lista)

    # Zapisanie danych zawodników
    for zawodnik in sumo_zawodnicy:
        lista = [zawodnik["Imie"], zawodnik["Nazwisko"], zawodnik["Kraj"], zawodnik["Waga"], zawodnik["Wzrost"]]
        print(zawodnik["Waga"])
        csv_writer.writerow(lista)

atrybuty_sumo =[]
naglowek = ["Imie", "Nazwisko", "Kraj", "Waga", "Wzrost"]
atrybuty_sumo.append(naglowek)

# Dodanie danych zawodników
for zawodnik in sumo_zawodnicy:
    atrybuty = [zawodnik["Imie"], zawodnik["Nazwisko"], zawodnik["Kraj"], zawodnik["Waga"], zawodnik["Wzrost"]]
    atrybuty_sumo.append(atrybuty)

# Wydrukowanie listy atrybutów
#for wiersz in atrybuty_sumo:
#    print(wiersz)
print(atrybuty_sumo)

# Otwarcie pliku do zapisu
with open(nazwa_pliku, mode='w', newline='') as file:
    csv_writer = csv.writer(file)

    # Zapisanie nagłówka
    lista = [[['Imie', 'Nazwisko', 'Kraj', 'Waga', 'Wzrost'],
              ['Hakuho', 'Sho', 'Mongolia', 154, 192],
              ['Kisenosato', 'Yutaka', 'Japonia', 178, 186],
              ['Asanoyama', 'Hideki', 'Japonia', 167, 188],
              ['Terunofuji', 'Haruo', 'Mongolia', 177, 191],
              ['Enho', 'Akira', 'Japonia', 98, 169]]]
    csv_writer.writerows(lista)