try:
    vuosi = int(input("Anna vuosiluku: "))
    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        print(f"{vuosi} on karkausvuosi.")
    else:
        print(f"{vuosi} ei ole karkausvuosi.")
except ValueError:
    print("Virheellinen syöte. Anna vuosiluku kokonaislukuna.")

