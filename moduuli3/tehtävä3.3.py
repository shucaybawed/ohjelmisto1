sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ").strip().lower()
try:
    hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
    if sukupuoli == "nainen":
        if hemoglobiini < 117:
            print("Hemoglobiiniarvo on alhainen.")
        elif hemoglobiini <= 175:
            print("Hemoglobiiniarvo on normaali.")
        else:
            print("Hemoglobiiniarvo on korkea.")
    elif sukupuoli == "mies":
        if hemoglobiini < 134:
            print("Hemoglobiiniarvo on alhainen.")
        elif hemoglobiini <= 195:
            print("Hemoglobiiniarvo on normaali.")
        else:
            print("Hemoglobiiniarvo on korkea.")
    else:
        print("Virheellinen sukupuoli. Anna 'mies' tai 'nainen'.")
except ValueError:
    print("Virheellinen hemoglobiiniarvo. Anna se kokonaislukuna.")

