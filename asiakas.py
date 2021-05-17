## Asiakas-luokka

class Asiakas:

    # Asiakkaalla on seuraavat tiedot tietokantataulussa nimeltä asiakas:
    # asnro - asiakasnumero, text, pk
    # snimi - sukunimi, text, nn
    # enimi - etunimi, text
    # email - sähköpostiosoite, text
    # puh   - puhelinnumero, text

    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()


    # Asiakkaan haku asiakasnumerolla
    # Tämän sisällä kutsutaan TulostaAsiakas()
    def HaeAsiakasNumerolla(self, _hakunro):
        try:
            hakulause = "SELECT * FROM asiakas where asnro = '" + _hakunro + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaAsiakas(rivi)
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))

    # Asiakkaan haku sukunimellä
    def HaeAsiakasNimella(self, _hakunimi):
        try:
            hakulause = "SELECT * FROM asiakas where snimi = '" + _hakunimi + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaAsiakas(rivi)
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))
      

    def HaeKaikkiAsiakkaat(self):   # Haetaan kaikki asiakkaat, tämän sisällä kutsutaan TulostaAsiakas()
        try:
            self.cur.execute("SELECT * FROM asiakas")
            rivit = self.cur.fetchall()
            self.TulostaAsiakas(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan asiakas-taulusta: {}.".format(e)) 


    def TulostaAsiakas(self, rivit):   # Tänne parametrina rivit, jotka SELECT on hakenut

        for rivi in rivit:
            print("Asiakasnumero: ", rivi[0])
            print("Nimi: ", rivi[2], " ", rivi[1])
            print("Yhteystiedot - email: ", rivi[3], " puhelin: ", rivi[4], "\n")
           

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