class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        self.nopeus = min(nopeus, self.huippunopeus)

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


s1 = Sähköauto("ABC-15", 180, 52.5)
p1 = Polttomoottoriauto("ACD-123", 165, 32.3)

s1.aseta_nopeus(150)
p1.aseta_nopeus(120)

s1.aja(3)
p1.aja(3)

print(s1.matkamittari)
print(p1.matkamittari)
