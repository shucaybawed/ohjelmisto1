luvut = []
while True:
    syöte = input("Anna luku (tai tyhjä lopettaaksesi): ")
    if syöte == "":
        break
    luvut.append(int(syöte))

luvut.sort(reverse=True)
print("Viisi suurinta:")
for luku in luvut[:5]:
    print(luku)
