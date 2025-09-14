def gallonat_litroiksi(gallona):
    return gallona * 3.785

while True:
    gallonat = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))
    if gallonat < 0:
        break
    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa = {litrat:.2f} litraa")
