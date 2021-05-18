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
        header1, header2, header3 = [
            'Tuotenumero',
            'Nimi',
            'Kuvaus']
        print(f'\n{header1:<15}{header2:<20}{header3:<40}')
        for rivi in rivit:
            print(f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:40}')


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
                    enimi || ' ' || snimi AS nimi, 
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
                    enimi || ' ' || snimi AS nimi, 
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
            header1, header2, header3, header4, header5, header6, header7 = [
                'Tuotenumero',
                'Nimi',
                'Kuvaus',
                'Tilausnro',
                'Pvm',
                'Asiakas',
                'Kpl']
            for rivi in rivit:
                if eka:
                    print(f'\n{header1:15}{header2:20}{header3:32}')
                    print(f'{rivi[0]:15}{rivi[1]:20}{rivi[2]:32}')
                    print(f'{header4:15}{header5:20}{header6:20}{header7:12}')
                    eka = False
                print(f'{rivi[3]:15}{rivi[4]:20}{rivi[5]:20}{rivi[6]:<12}')
        except Exception as e:
            print(f"Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {e}.")
