import random
n = int(input("Arpakuutioiden määrä: "))
summa = 0
for i in range(n):
    summa += random.randint(1, 6)

print("Silmälukujen summa:", summa)
