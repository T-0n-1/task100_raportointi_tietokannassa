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
            self.cur.execute("SELECT asnro, enimi || ' ' || snimi, email, puh FROM asiakas")
            rivit = self.cur.fetchall()
            self.TulostaAsiakas(rivit)
        except Exception as e:
            print(f"Rivejä ei pystytty lukemaan asiakas-taulusta: {e}.")


    def TulostaAsiakas(self, rivit):   # Tänne parametrina rivit, jotka SELECT on hakenut
        ta1, ta2, ta3, ta4 = ['Asiakasnumero', 'Nimi', 'Email', 'Puhelin']
        print(f'\n{ta1:<15}{ta2:<20}{ta3:<30}{ta4}')
        for rivi in rivit:
            print(f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:30}{rivi[3]}')
           

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