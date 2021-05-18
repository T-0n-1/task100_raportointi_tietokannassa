class tuote:
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
            print(f'\n{"Tuotenumero":<15}{"Nimi":<20}{"Kuvaus":<40}')
            for rivi in rivit:
                print(f"{rivi[0]:15}{rivi[1]:20}{rivi[2]:40}")
        except:
            pass

    def TulostaTuotteenTilausrivit(self, _hakunro):
        eka = True
        try:
            if _hakunro.isdigit():
                hakulause = f"""
                SELECT 
                    tu.tuotenro, 
                    nimi, 
                    kuvaus, 
                    tr.tilausnro, 
                    pvm, 
                    snimi || ' ' || enimi AS nimi, 
                    kpl 
                FROM tuote tu 
                JOIN tilausrivi tr 
                    USING (tuotenro) 
                JOIN tilaus ti 
                    USING (tilausnro) 
                JOIN asiakas a 
                    USING (asnro) 
                WHERE tu.tuotenro = '{_hakunro}'"""
            else:
                hakulause = f"""
                SELECT 
                    tu.tuotenro, 
                    nimi, 
                    kuvaus, 
                    tr.tilausnro, 
                    pvm, 
                    snimi || ' ' || enimi AS nimi, 
                    kpl 
                FROM tuote tu 
                JOIN tilausrivi tr 
                    USING (tuotenro) 
                JOIN tilaus ti 
                    USING (tilausnro) 
                JOIN asiakas a 
                    USING (asnro)  
                WHERE tu.tuotenro = 
                    (SELECT tuotenro FROM tuote WHERE nimi = '{_hakunro}')"""
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            if rivit == []:
                print("Ei raportoitavaa")
            for rivi in rivit:
                if eka:
                    print(f'\n{"Tuotenumero":15}{"Nimi":20}{"Kuvaus":32}')
                    print(f"{rivi[0]:15}{rivi[1]:20}{rivi[2]:32}")
                    print(f'{"Tilausnro":15}{"Pvm":20}{"Asiakas":20}{"Kpl":12}')
                    eka = False
                print(f"{rivi[3]:15}{rivi[4]:20}{rivi[5]:20}{rivi[6]:<12}")
        except:
            print("Ei raportoitavaa")
