while True:
 tuumat = float(input("anna tuuma määrä (negatiivinen lopettaa):"))
 if tuumat < 0:
     print ("ohjelma lopetetaan.")
     break

senttimetrit = tuumat * 2,54
print(f"{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä")