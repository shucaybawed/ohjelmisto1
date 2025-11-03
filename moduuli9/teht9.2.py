class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


auto = Auto("OG-45", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")

auto.kiihdytä(-200)
print(f"Hätäjarrutuksen jälkeen nopeus: {auto.nopeus} km/h")
