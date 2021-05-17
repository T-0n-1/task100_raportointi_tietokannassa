## Tilaus-luokka

class Tilaus:
    # Tilauksella on seuraavat tiedot tietokantataulussa nimeltä tilaus:
    # tilausnro - tilausnumero, text, pk
    # pvm       - tilauksen päivämäärä(muodossa ppkkvvvv), text, nn
    # asnro     - tilauksen tehneen asiakkaan asiakasnumero, nn, f(oreign)key(viittaa asiakas -tauluun)

    # Parametrisoitu muodostinfunktio - constructor
    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()


    # Haetaan kaikki tilaukset
    # Tämän sisällä kutsutaan TulostaTilaus()
    def HaeKaikkiTilaukset(self):
        try:
            self.cur.execute("SELECT asiakas.snimi, pvm, tilausnro FROM tilaus, asiakas where asiakas.asnro = tilaus.asnro")
            rivit = self.cur.fetchall()
            self.TulostaTilaus(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tilaus-taulusta: {}.".format(e)) 

    # Tulostetaan 1 asiakas kerrallaan
    # Tänne parametrina rivit, jotka select on hakenut
    def TulostaTilaus(self, rivit):
        for rivi in rivit:
            print("Asiakas: ", rivi[0], " tilausnumero: ", rivi[2], " tilauspvm:", rivi[1])
