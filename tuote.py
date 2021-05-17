# Määrittele importit


# Määrittele luokat
class Tuote:
    # Tuotteella on seuraavat tiedot tietokantataulussa nimeltä tuote:
    # tuotenro - tuotenumero, text, pk
    # nimi - selkokielinen nimi, text, nn
    # kuvaus - tuotteen kuvausteksti, text


    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()


    def HaeKaikkiTuotteet(self):
        try:
            self.cur.execute("SELECT * FROM tuote")
            rivit = self.cur.fetchall()
            self.TulostaTuote(rivit)
        except Exception as e:
            print(f"Rivejä ei pystytty lukemaan tuote-taulusta: {e}.")


    def TulostaTuote(self, rivit):
        tt1, tt2, tt3 = ['Tuotenumero', 'Nimi', 'Kuvaus']
        print(f'\n{tt1:<15}{tt2:<20}{tt3:<40}')
        for rivi in rivit:
            print(f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:40}')
           

    # Tulostetaan 1 asiakkaan kaikki tilaukset
    def TulostaAsiakkaanTilaukset(self, _hakunro):
        eka = True
        try:
            hakulause = "SELECT asiakas.asnro, tilausnro, pvm FROM asiakas, tilaus where asiakas.asnro = tilaus.asnro and asiakas.asnro = '" + _hakunro + "'"
            self.cur.execute(hakulause)  
            rivit = self.cur.fetchall()
            for rivi in rivit:
                if (eka):
                    print("Asiakasnumero:   ", rivi[0])
                    eka = False
                print("   tilausnumero: ", rivi[1], " tilauspvm", rivi[2])
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {}.".format(e))