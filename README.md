# task100_raportointi_tietokannassa
100. Asiakkaiden, tuotteiden ja tilausten raportointi kauppa.db tietokannassa

Tee sovellus, jolla voit tuottaa asiakas-, tuote- ja tilausraportteja kauppa.db-tietokannasta. Tietokanta on sama, jota on käsitelty videoiden esimerkeissä. Huomaa, että VPL ei hae omasta hakemistopolustasi, joten esittele tietokanta näin: tietokanta = "kauppa.db"

Hyväksyttyyn arvosanaan minimivaatimuksena on, että ohjelman suorituksessa ei ole virheitä, vaaditut luokkamääritykset on tehty ja vähintään kaksi raporttia toimii määritysten mukaan. Tämän jälkeen jokaisesta määritysten mukaisesti toimivasta raportista saa yhden arvosanan lisää.

Sovellus on toteutettava olio-ohjelmointia käyttäen, pääohjelma on löydyttävä tiedostosta ratkaisu.py ja siitä on löydyttävä ainakin seuraavat luokkamääritykset:

Tiedostossa asiakas.py luokka asiakas
Tiedostossa tuote.py luokka tuote
Tiedostossa tilaus.py luokka tilaus
Lisäksi on löydyttävä ainakin seuraavat oliomuuttujat:

Tiedostossa ratkaisu.py luokan asiakas oliomuuttuja asi
Tiedostossa ratkaisu.py luokan tuote oliomuuttuja tte
Tiedostossa ratkaisu.py luokan tilaus oliomuuttuja til
Olioiden luonnit ratkaisu.py tiedostossa täytyy tehdä kaikki ennen pääohjelmasilmukkaa, koska botti tarkastaa suorituksen jälkeen, että kaikki oliot on luotu. Jos oliot luodaan vasta valintojen suorituksen yhteydessä, niin jokin olio saattaa jäädä luomatta ja botin virheilmoitus generoituu siitä eikä tarkastus mene läpi.

Sovelluksen toiminta on seuraavanlainen:

Tulostetaan useampirivinen valikkoteksti ja komentokehote 'Anna valinta: '
Luetaan valinta
Mikäli valinta ei ole sallittu niin
tulostetaan virheteksti 'Virheellinen valinta'
Mikäli valinta on sallittu, mutta ei lopetus niin
Luetaan valinnan mahdollinen hakuehto komentokehotteella 'Hakuehto: '
Mikäli hakuehdolla löytyy raportoitavaa niin
Tulostetaan haluttu raportti (listaus)
Mikäli ei löydy raportoitavaa niin
Tulostetaan teksti 'Ei raportoitavaa'
Palataan valikkotekstin tulostukseen
Mikäli valinta on sovelluksen lopetus niin
Tulostetaan teksti 'Sovellus lopetetaan' ja
Lopetetaan sovellus

Sovelluksella on tuotettava seuraavat raportit:
Listaus kaikista asiakkaista
Tulostetaan
Sarakeotsikot omalle rivilleen
Asiakastiedot omille riveilleen
Asiakasnumero, nimi, sähköpostitunnus ja puhelinnumero
Listaus kaikista tuotteista
Tulostetaan
Sarakeotsikot omalle rivilleen
Tuotetiedot omille riveilleen
Tuotenumero, nimi ja kuvaus
Listaus kaikista hakukriteerinä olevan asiakkaan tilauksista
Hakukriteerinä asiakaan nimi tai asiakasnumero
Tulostetaan
Asiakkaan asiakasnumero ja nimi omalle riville
Tilaustietojen sarakeotsikot omalle rivilleen
Asiakkaan kaikkien tilausten tiedot omille riveilleen
Tilausnumero ja tilauspäivämäärä
Listaus kaikista hakukriteerinä olevan tuotteen tilausten tilausriveistä
Hakukriteerinä tuotteen nimi tai tuotenumero
Tulostetaan
Tuotteen tuotenumero, nimi ja kuvaus omalle rivilleen
Tilaustietojen sarakeotsikot omalle rivilleen
Tilaustiedot omille riveilleen
Tilausnumero, asiakkaan nimi,  tilauspäivämäärä ja kappalemäärä
Listaus hakuriteerinä olevan tilauksen tilausriveistä
Hakukriteerinä tilausnumero
Tulostetaan
Tilausnumero, asiakas ja tilauspäivämäärä omalle rivilleen
Tilausrivien otsikkotiedot omalle rivilleen
Tilausrivitiedot omille riveilleen
Tuotenumero, tuotteen nimi
Listaus kaikista tilauksista halutusta päivämäärästä lähtien
Hakukriteerinä
Alkupäivämäärä
Tulostetaan
Alkupäivämäärä omalle rivilleen
Tilaustietojen sarakeotsikot omalle rivilleen
Tilausten tiedot omille riveilleen
Asiakasnumero, asikkaan nimi, tilausnumero ja tilauspäivämäärä
Huom! Seuraavat varoitukset evaluoinnin tuloksissa eivät vaikuta arviointiin:

vpl_evaluate.cpp: In member function ‘void Evaluation::runTests()’: vpl_evaluate.cpp:1648:115: warning: format ‘%lu’ expects argument of type ‘long unsigned int’, but argument 2 has type ‘size_t {aka unsigned int}’ [-Wformat=] printf("Testing %lu/%lu : %s\n", i+1, (unsigned long)testCases.size(), testCases[i].getCaseDescription().c_str());

Seuraavassa käyttöliittymäesimerkki
Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 7
Virheellinen valinta

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 1

Asiakasnumero  Nimi                Email                         Puhelin
1111           Ahonen Antti        antti.ahonen@labi.fi          0401234567
2222           Eerola Erkki        erkki.eerola@hopo.fi          0402345678
3333           Kilpi Kaarina       kaarina.kilpi@jees.fi         0449876543
4444           Mallila Milla       milla.mallila@hups.fi         None

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 2

Tuotenumero    Nimi                Kuvaus
0010           pulikka             Karjalanpiirakoiden tekoväline.
0020           nappu               Löylyn heittoon.
0030           tuura               Jään rikkomiseen ja ison avannon tekoon.

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 3
Hakuehto: 1234
Ei raportoitavaa

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 3
Hakuehto: 2222

Asiakasnumero  Nimi                Email                         Puhelin
2222           Eerola Erkki        erkki.eerola@hopo.fi          0402345678
Tilausnro      Pvm
100523         01012020
100592         01022020

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 4
Hakuehto: 0010

Tuotenumero    Nimi                Kuvaus
0010           pulikka             Karjalanpiirakoiden tekoväline.
Tilausnro      Pvm                 Asiakas             Kpl
100152         01012020            Ahonen Antti        1
100592         01022020            Eerola Erkki        1
100801         13022020            Kilpi Kaarina       10

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 5
Hakuehto: 100152

Tilausnumero   Pvm                 Asiakasnumero
100152         01012020            1111
Tuotenumero    Kpl
0010           1
0020           1

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 6
Hakuehto: 01022020

Tilausnumero   Pvm                 Asiakasnumero
100592         01022020            2222
100801         13022020            3333
101410         14022020            4444
101839         16022020            4444

Kauppa-tietokannan raportointisovellus
1 - Listaa kaikki asiakkaat
2 - Listaa kaikki tuotteet
3 - Listaa kaikki halutun asiakkaan tilaukset
4 - Listaa kaikki halutun tuotteen tilaukset
5 - Listaa halutun tilauksen tilausrivit
6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien
0 - Lopeta
Anna valinta: 0
Sovellus lopetetaan
