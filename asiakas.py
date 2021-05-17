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


    def HaeKaikkiAsiakkaat(self):
        try:
            self.cur.execute("SELECT asnro, enimi || ' ' || snimi, email, puh FROM asiakas")
            rivit = self.cur.fetchall()
            self.TulostaAsiakas(rivit)
        except Exception as e:
            print(f"Rivejä ei pystytty lukemaan asiakas-taulusta: {e}.")


    def TulostaAsiakas(self, rivit):
        header1, header2, header3, header4 = ['Asiakasnumero', 'Nimi', 'Email', 'Puhelin']
        print(f'\n{header1:<15}{header2:<20}{header3:<30}{header4}')
        for rivi in rivit:
            print(f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:30}{rivi[3]}')
           

    def TulostaAsiakkaanTilaukset(self, _hakunro):
        try:
            if _hakunro.isdigit():
                hakulause = f"SELECT a.asnro, enimi || ' ' || snimi AS nimi, email, puh, tilausnro, pvm FROM asiakas a, tilaus t WHERE a.asnro = t.asnro AND a.asnro = {_hakunro}"
            else:
                etunimi, sukunimi = _hakunro.split()
                hakulause = f"SELECT a.asnro, enimi || ' ' || snimi AS nimi, email, puh, tilausnro, pvm FROM asiakas a, tilaus t WHERE a.asnro = t.asnro AND a.asnro = (SELECT asnro FROM asiakas WHERE (enimi = '{etunimi}' AND snimi = '{sukunimi}'))"
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            header1, header2, header3, header4, header5, header6 = ['Asiakasnumero', 'Nimi', 'Email', 'Puhelin', 'Tilausnro', 'Pvm']
            tilaukset = []
            for rivi in rivit:
                rivi1 = f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:30}{rivi[3]:10}'
                rivi2 = f'{rivi[4]:15}{rivi[5]:20}'
                tilaukset.append(rivi2)
            print(f'\n{header1:15}{header2:20}{header3:30}{header4:10}')
            print(rivi1)
            print(f'{header5:15}{header6:20}')
            for rivi in tilaukset:
                print(rivi)
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {}.".format(e))