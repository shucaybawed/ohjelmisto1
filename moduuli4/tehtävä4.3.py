luku = input("anna luku")
pienin = int(luku)
suurin = int(luku)
while luku != "":
    if int(luku) < pienin:
        pienin = int(luku)
    if int(luku) > suurin:
        suurin = int(luku)
    luku = input("anna luku")
print(f"Pienin luku: {pienin}")
print(f"Suurin luku: {suurin}")



