import random

def heita_noppa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

tahkot = int(input("Anna nopan tahkojen määrä: "))
while True:
    silmaluku = heita_noppa(tahkot)
    print(f"Heitto: {silmaluku}")
    if silmaluku == tahkot:
        break
