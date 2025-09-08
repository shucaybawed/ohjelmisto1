import random

N = int(input("Pisteiden määrä: "))
n = 0

for i in range(N):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x*x + y*y < 1:
        n += 1

print(4 * n / N)
