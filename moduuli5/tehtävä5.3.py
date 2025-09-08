n = int(input("Anna kokonaisluku: "))

if n < 2:
    print("Ei ole alkuluku")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Ei ole alkuluku")
            break
    else:
        print("On alkuluku")
