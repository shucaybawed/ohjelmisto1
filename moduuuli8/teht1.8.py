import mysql.connector

yhteys = mysql.connector.connect(
         host= 'localhost',
         port= 3306,
         database='flight_game',
         user='user',
         password='dametime',
         autocommit=True)






import sqlite3

icao = input("Anna ICAO-koodi: ").strip().upper()

conn = sqlite3.connect("flight_game.db")
cur = conn.cursor()

cur.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
result = cur.fetchone()

if result:
    print(f"Nimi: {result[0]}, Kunta: {result[1]}")
else:
    print("Lentokenttää ei löytynyt.")

conn.close()

