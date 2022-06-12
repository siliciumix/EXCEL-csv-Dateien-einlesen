import csv

kopfzeile = True
#kopfzeile = False

with open("Beispiel.csv", "r", encoding="utf-8") as csv_datei:
    reader = csv.reader(csv_datei, delimiter=";")

    # Ist die Variable kopfzeile auf True wird diese auch mit ausgeben.
    # andernfalls wird die Kopfzeile übersprungen.
    if kopfzeile != True:
        next(reader)

    for zeile in reader:
        print(f"{zeile[0]} | {zeile[1]} | {zeile[3]} | {zeile[3]}")
