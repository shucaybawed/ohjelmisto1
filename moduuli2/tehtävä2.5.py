leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luodit_yhteensa * 13.3
kilogrammat = int(grammat // 1000)
grammat_jaljella = grammat % 1000
print(f"\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat_jaljella:.2f} grammaa")
