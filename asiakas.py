class asiakas:
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
            self.cur.execute(
                """
            SELECT 
                asnro, 
                snimi || ' ' || enimi, 
                email, 
                puh 
            FROM asiakas"""
            )
            rivit = self.cur.fetchall()
            print(f'\n{"Asiakasnumero":<15}{"Nimi":<20}{"Email":<30}{"Puhelin"}')
            for rivi in rivit:
                print(f"{rivi[0]:15}{rivi[1]:20}{rivi[2]:30}{rivi[3]}")
        except:
            pass

    def TulostaAsiakkaanTilaukset(self, _hakunro):
        eka = True
        try:
            if _hakunro.isdigit():
                hakulause = f"""
                SELECT 
                    a.asnro, 
                    snimi || ' ' || enimi AS nimi, 
                    email, 
                    puh, 
                    tilausnro, 
                    pvm 
                FROM asiakas a, tilaus t 
                WHERE a.asnro = t.asnro 
                    AND a.asnro = {_hakunro}"""
            else:
                nimi1, nimi2 = _hakunro.split()
                hakulause = f"""
                SELECT 
                    a.asnro, 
                    snimi || ' ' || enimi AS nimi, 
                    email, 
                    puh, 
                    tilausnro, 
                    pvm 
                FROM asiakas a, tilaus t 
                WHERE a.asnro = t.asnro 
                    AND a.asnro = 
                        (SELECT 
                            asnro 
                        FROM asiakas 
                        WHERE (enimi = '{nimi1}' AND snimi = '{nimi2}')
                        OR (enimi = '{nimi2}' AND snimi = '{nimi1}'))"""
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            if rivit == []:
                print("Ei raportoitavaa")
            for rivi in rivit:
                if eka:
                    print(f'\n{"Asiakasnumero":15}{"Nimi":20}{"Email":30}{"Puhelin":10}')
                    print(f"{rivi[0]:15}{rivi[1]:20}{rivi[2]:30}{rivi[3]}")
                    print(f'{"Tilausnro":15}{"Pvm":20}')
                    eka = False
                print(f"{rivi[4]:15}{rivi[5]:20}")
        except:
            print("Ei raportoitavaa")
