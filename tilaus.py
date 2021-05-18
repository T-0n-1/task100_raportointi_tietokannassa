class Tilaus:
    # Tilauksella on seuraavat tiedot tietokantataulussa nimeltä tilaus:
    # tilausnro - tilausnumero, text, pk
    # pvm       - tilauksen päivämäärä(muodossa ppkkvvvv), text, nn
    # asnro     - tilauksen tehneen asiakkaan asiakasnumero, nn, f(oreign)key(viittaa asiakas -tauluun)


    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()


    def HaeKaikkiTilaukset(self):
        try:
            self.cur.execute("SELECT asiakas.snimi, pvm, tilausnro FROM tilaus, asiakas where asiakas.asnro = tilaus.asnro")
            rivit = self.cur.fetchall()
            self.TulostaTilaus(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tilaus-taulusta: {}.".format(e)) 


    def TulostaTilaus(self, rivit):
        for rivi in rivit:
            print("Asiakas: ", rivi[0], " tilausnumero: ", rivi[2], " tilauspvm:", rivi[1])


    def TulostaTilauksenTilausrivit(self, _hakunro):
        eka = True
        try:
            hakulause = f"""
            SELECT 
                ti.tilausnro,
                pvm,
                asnro,
                tuotenro,
                kpl
            FROM tilaus ti,
                tilausrivi tr
            WHERE ti.tilausnro = tr.tilausnro
                AND ti.tilausnro = '{_hakunro}'"""
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            header1, header2, header3, header4, header5 = [
                'Tilausnumero',
                'Pvm',
                'Asiakasnumero',
                'Tuotenumero',
                'Kpl']
            for rivi in rivit:
                if eka:
                    print(f'\n{header1:15}{header2:20}{header3:13}')
                    print(f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:13}')
                    print(f'{header4:15}{header5:20}')
                    eka = False
                print(f'{rivi[3]:15}{rivi[4]:<20}')
        except Exception as e:
            print(f"Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {e}.")


    def TulostaTilauksetPvm(self, _hakunro):
        eka = True
        try:
            hakulause = f"""
            SELECT 
                tilausnro,
                pvm,
                asnro
            FROM tilaus t
            WHERE pvm >= '{_hakunro}'"""
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            header1, header2, header3 = [
                'Tilausnumero',
                'Pvm',
                'Asiakasnumero']
            for rivi in rivit:
                if eka:
                    print(f'\n{header1:15}{header2:20}{header3:13}')
                    eka = False
                print(f'{rivi[0]:15}{rivi[1]:<20}{rivi[2]:13}')
        except Exception as e:
            print(f"Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {e}.")