# Määrittele importit
import sqlite3
from sqlite3 import Error

from asiakas import Asiakas
from tilaus import Tilaus
from tuote import Tuote


# Määrittele luokat
def create_connection(db_file):
    ## Esimerkki sivustolta: https://www.sqlitetutorial.net/sqlite-python/
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def valikko():   # Funktio, joka tulostaa valikon, ja palauttaa tehdyn valinnan
    print("\n1 - tulosta kaikki asiakkaat")
    print("2 - hae ja tulosta asiakas sukunimen perusteella")
    print("3 - hae ja tulosta asiakas asiakasnumeron perusteella")
    print("4 - tulosta kaikki tilaukset")
    print("5 - tulosta yhden asiakkaan tilaukset")
    print("0 - lopeta")
    jatka = input("? ")
    return jatka


# Olioiden määrittely (oliomuuttujat asi, tte ja til) Voikohan valikko-funktio olla tämän yläpuolella



### PÄÄOHJELMA ###

## Laita tähän se polku, jossa kauppa.db on omalla koneellasi
tietokanta = r"kauppa.db"

# luodaan yhteys tietokantaan
conn = create_connection(tietokanta)
 
if conn is not None:  # Mikäli tietokantayhteys saatiin luotua:
       
    jatka = valikko()
    while jatka != "0":
        if jatka == "1":
            asiakas = Asiakas(conn)
            asiakas.HaeKaikkiAsiakkaat()
        elif jatka == "2":
            asiakas = Asiakas(conn)
            nimi = input("Anna asiakkaan sukunimi: ")
            asiakas.HaeAsiakasNimella(nimi)
        elif jatka == "3":
            asiakas = Asiakas(conn)
            numero = input("Anna asiakkaan asiakasnumero: ")
            asiakas.HaeAsiakasNumerolla(numero)
        elif jatka == "4":
            tilaus = Tilaus(conn)
            tilaus.HaeKaikkiTilaukset()
        elif jatka == "5":
            asiakas = Asiakas(conn)
            numero = input("Anna asiakkaan asiakasnumero: ")
            asiakas.TulostaAsiakkaanTilaukset(numero)
        else:
            print("Tarkista valintasi")

        jatka = valikko()
            
    conn.close()   # suljetaan yhteys

else:
    print("Virhe! Yhteyttä tietokantaan ei voida luoda.")




