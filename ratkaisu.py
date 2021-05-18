# Määrittele importit
import sqlite3
from sqlite3 import Error

from asiakas import Asiakas
from tilaus import Tilaus
from tuote import Tuote


import asiakas, tilaus, tuote

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


def valikko(): 
    print('\nKauppa-tietokannan raportointisovellus')
    print("1 - Listaa kaikki asiakkaat")
    print('2 - Listaa kaikki tuotteet')
    print("3 - Listaa kaikki halutun asiakkaan tilaukset")
    print("4 - Listaa kaikki halutun tuotteen tilaukset")
    print("5 - Listaa halutun tilauksen tilausrivit")
    print("6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien")
    print("0 - Lopeta")
    jatka = input("Anna valinta: ")
    return jatka


# Olioiden määrittely (oliomuuttujat asi, tte ja til) Voikohan valikko-funktio olla tämän yläpuolella



### PÄÄOHJELMA ###
tietokanta = r"kauppa.db"   # Tietokannan sijainnin määrittely
conn = create_connection(tietokanta)   # Yhteys tietokantaan
if conn is not None:  # Mikäli tietokantayhteys saatiin luotua:

    jatka = valikko()
    while jatka != "0":
        if jatka == "1":
            asiakas = Asiakas(conn)
            asiakas.HaeKaikkiAsiakkaat()
        elif jatka == "2":
            tuote = Tuote(conn)
            tuote.HaeKaikkiTuotteet()
        elif jatka == "3":
            asiakas = Asiakas(conn)
            hakuehto = input("Hakuehto: ")
            asiakas.TulostaAsiakkaanTilaukset(hakuehto)
        elif jatka == "4":
            tuote = Tuote(conn)
            hakuehto = input("Hakuehto: ")
            tuote.TulostaTuotteenTilausrivit(hakuehto)
        elif jatka == "5":
            tilaus = Tilaus(conn)
            hakuehto = input("Hakuehto: ")
            tilaus.TulostaTilauksenTilausrivit(hakuehto)
        elif jatka == "6":
            tilaus = Tilaus(conn)
            hakuehto = input("Hakuehto: ")
            tilaus.TulostaTilauksetPvm(hakuehto)
        else:
            print("Virheellinen valinta")

        jatka = valikko()
            
    conn.close()   # suljetaan yhteys

else:
    print("Virhe! Yhteyttä tietokantaan ei voida luoda.")




