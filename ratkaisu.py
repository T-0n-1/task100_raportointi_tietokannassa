# Määrittele importit
import sqlite3

from asiakas import asiakas
from tilaus import tilaus
from tuote import tuote


# Määrittele luokat
def valikko():
    print("\nKauppa-tietokannan raportointisovellus")
    print("1 - Listaa kaikki asiakkaat")
    print("2 - Listaa kaikki tuotteet")
    print("3 - Listaa kaikki halutun asiakkaan tilaukset")
    print("4 - Listaa kaikki halutun tuotteen tilaukset")
    print("5 - Listaa halutun tilauksen tilausrivit")
    print("6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien")
    print("0 - Lopeta")
    jatka = input("Anna valinta: ")
    return jatka


### PÄÄOHJELMA ###
conn = None
with sqlite3.connect("kauppa.db") as conn:
    if conn is not None:
        asi = asiakas(conn)
        tte = tuote(conn)
        til = tilaus(conn)

        jatka = valikko()
        while jatka != "0":
            if jatka == "1":
                asi.HaeKaikkiAsiakkaat()
            elif jatka == "2":
                tte.HaeKaikkiTuotteet()
            elif jatka == "3":
                hakuehto = input("Hakuehto: ")
                asi.TulostaAsiakkaanTilaukset(hakuehto)
            elif jatka == "4":
                hakuehto = input("Hakuehto: ")
                tte.TulostaTuotteenTilausrivit(hakuehto)
            elif jatka == "5":
                hakuehto = input("Hakuehto: ")
                til.TulostaTilauksenTilausrivit(hakuehto)
            elif jatka == "6":
                hakuehto = input("Hakuehto: ")
                til.TulostaTilauksetPvm(hakuehto)
            else:
                print("Virheellinen valinta")
            jatka = valikko()
        print("Sovellus lopetetaan")
    else:
        print("Virhe! Yhteyttä tietokantaan ei voida luoda.")
