vuodenajat = (
    "talvi", "talvi", "talvi",
    "kevät", "kevät", "kevät",
    "kesä", "kesä", "kesä",
    "syksy", "syksy", "syksy"
)

k = int(input("Anna kuukauden numero (1-12): "))
if 1 <= k <= 12:
    print(vuodenajat[k % 12])
else:
    print("Virheellinen numero")
