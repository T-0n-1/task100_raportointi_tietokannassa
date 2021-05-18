class tilaus:
    # Tilauksella on seuraavat tiedot tietokantataulussa nimeltä tilaus:
    # tilausnro - tilausnumero, text, pk
    # pvm       - tilauksen päivämäärä(muodossa ppkkvvvv), text, nn
    # asnro     - tilauksen tehneen asiakkaan asiakasnumero, nn,
    #             f(oreign)key(viittaa asiakas -tauluun)

    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()

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
            if rivit == []:
                print("Ei raportoitavaa")
            for rivi in rivit:
                if eka:
                    print(f'\n{"Tilausnumero":15}{"Pvm":20}{"Asiakasnumero":13}')
                    print(f"{rivi[0]:15}{rivi[1]:20}{rivi[2]:13}")
                    print(f'{"Tuotenumero":15}{"Kpl":20}')
                    eka = False
                print(f"{rivi[3]:15}{rivi[4]:<20}")
        except:
            print("Ei raportoitavaa")

    def TulostaTilauksetPvm(self, _hakunro):
        eka = True
        try:
            hakulause = f"""
            SELECT 
                tilausnro,
                pvm,
                asnro
            FROM tilaus t
            WHERE 
                (SUBSTR(pvm, 5, 4) ||
                SUBSTR(pvm, 3, 2) ||
                SUBSTR(pvm, 1, 2))
                >=
                (SUBSTR({_hakunro}, 5, 4) ||
                SUBSTR({_hakunro}, 3, 2) ||
                SUBSTR({_hakunro}, 1, 2))"""
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            if rivit == []:
                print("Ei raportoitavaa")
            for rivi in rivit:
                if eka:
                    print(f'\n{"Tilausnumero":15}{"Pvm":20}{"Asiakasnumero":13}')
                    eka = False
                print(f"{rivi[0]:15}{rivi[1]:<20}{rivi[2]:13}")
        except:
            print("Ei raportoitavaa")
