nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

for n in nimet:
    print(n)
