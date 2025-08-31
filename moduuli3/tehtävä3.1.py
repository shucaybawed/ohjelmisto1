pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen!")
    print(f"Kuhaalta puuttuu {puuttuu} cm alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallitun mittainen. Saat pitää sen.")
