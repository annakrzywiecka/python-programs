import csv

#wczytujemy plik podając ścieżkę i nadajemy wczytanemu plikowi nazwę, np. sumo, następnie wczytujemy do zmiennej
with open(r'C:\Users\Ania\Desktop\sumo.csv') as sumo: #r - jako raw, aby nie rozumiał specjalnie znaku \
    sumo_imported = csv.reader(sumo)
    naglowek = next(sumo_imported)

    #policzymy średnią wagę zawodników
    suma_mas = 0
    ilosc_zawodnikow = 0
    for row in sumo_imported:
        suma_mas += int(row[3])
        ilosc_zawodnikow += 1    
    if ilosc_zawodnikow != 0:
        srednia_masa = suma_mas/ilosc_zawodnikow
        print(srednia_masa)


results = [
    ['Osoba', 'Ocena'],
    ['Ola', 4],
    ['Tomasz', 3],
    ['Karolina', 5]
]

with open(r'C:\Users\Ania\Desktop\wyniki.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(results)


import csv

# Dane zawodników sumo
sumo_zawodnicy = [
    {"Imię": "Hakuho", "Nazwisko": "Sho", "Kraj": "Mongolia", "Waga": 154, "Wzrost": 192},
    {"Imię": "Kisenosato", "Nazwisko": "Yutaka", "Kraj": "Japonia", "Waga": 178, "Wzrost": 186},
    {"Imię": "Asanoyama", "Nazwisko": "Hideki", "Kraj": "Japonia", "Waga": 167, "Wzrost": 188},
    {"Imię": "Terunofuji", "Nazwisko": "Haruo", "Kraj": "Mongolia", "Waga": 177, "Wzrost": 191},
    {"Imię": "Enho", "Nazwisko": "Akira", "Kraj": "Japonia", "Waga": 98, "Wzrost": 169},
]


nazwa_pliku = r'C:\Users\Ania\Desktop\zawodnicy_sumo_stoworzne.csv'

# Otwarcie pliku do zapisu
with open(nazwa_pliku,  newline='') as file:
    csv_writer = csv.writer(file)

    # Zapisanie nagłówka
    csv_writer.writerow(["Imię", "Nazwisko", "Kraj", "Waga (kg)", "Wzrost (cm)"])

    # Zapisanie danych zawodników
    for zawodnik in sumo_zawodnicy:
        csv_writer.writerow(zawodnik["Imię"], zawodnik["Nazwisko"], zawodnik["Kraj"], zawodnik["Waga"], zawodnik["Wzrost"])
        print(zawodnik["Waga"])


