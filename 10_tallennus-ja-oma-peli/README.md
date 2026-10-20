# Osa 10 – Tallennus ja oma peli

Tämä on kurssin viimeinen vaihe.

Aiemmissa osissa rakensimme seikkailupeliin pelaajan, inventaarion, vihollisen, kaupan ja taistelun.

Nyt lisäämme peliin tallennuksen ja teemme pelistä lopuksi oman version.

## Tavoite

Opit:

- lukemaan tietoja tiedostosta
- kirjoittamaan tietoja tiedostoon
- käyttämään Pythonin `json`-moduulia
- tallentamaan sanakirjoja ja listoja
- yhdistämään aikaisemmin opittuja asioita omaksi peliksi

## Kokeile

Avaa tämän kansion `main.py` ja käynnistä ohjelma.

1. Aloita uusi peli.
2. Kerää esineitä tai osta terveysjuoma.
3. Taistele vihollista vastaan.
4. Valitse valikosta **Tallenna peli**.
5. Lopeta ohjelma.
6. Käynnistä se uudelleen ja jatka tallennettua peliä.

Ohjelma luo tallennustiedoston nimeltä `save.json`.

Tiedostoon tallennetaan pelaajan tiedot, vihollisen tiedot ja inventaario.

## Tutki

### 1. JSON-moduuli

Ohjelman alussa on:

```python
import json
```

`json` on Pythonin mukana tuleva moduuli, jonka avulla tietoja voidaan tallentaa ja lukea JSON-muodossa.

JSON sopii esimerkiksi sanakirjojen ja listojen tallentamiseen.

### 2. Pelin tallentaminen

Tallennusfunktiossa kootaan pelin tiedot sanakirjaan:

```python
game_data = {
    "player": player,
    "enemy": enemy,
    "inventory": inventory
}
```

Sen jälkeen tiedot kirjoitetaan tiedostoon:

```python
with open("save.json", "w", encoding="utf-8") as file:
    json.dump(game_data, file, ensure_ascii=False, indent=4)
```

Tässä:

- `open()` avaa tiedoston
- `"w"` tarkoittaa kirjoittamista
- `json.dump()` kirjoittaa tiedot JSON-muodossa
- `encoding="utf-8"` mahdollistaa esimerkiksi ääkköset

Jos tiedostoa ei vielä ole, Python luo sen.

### 3. Pelin lataaminen

Peli ladataan lukemalla tallennustiedosto:

```python
with open("save.json", "r", encoding="utf-8") as file:
    game_data = json.load(file)
```

Tässä `"r"` tarkoittaa lukemista.

`json.load()` muuttaa tiedoston JSON-tiedot takaisin Pythonin tietorakenteiksi.

Jos tallennustiedostoa ei löydy, ohjelma käsittelee tilanteen `FileNotFoundError`-poikkeuksella ja aloittaa uuden pelin.

### 4. Miksi `with`?

Kun tiedosto avataan `with`-rakenteella, Python huolehtii tiedoston sulkemisesta lohkon päätyttyä.

Tämä on hyvä tapa käsitellä tiedostoja.

## Muokkaa

Tee pelistä oman näköisesi.

Muuta esimerkiksi:

- pelin nimi ja tarina
- pelaajan aloitusterveys ja kulta
- vihollisen nimi ja ominaisuudet
- löydettävät esineet
- kaupan tuotteet
- taistelun säännöt

Kokeile muutoksia yksi kerrallaan ja testaa peliä jokaisen muutoksen jälkeen.

## Haaste

Lisää peliin uusi vihollinen tai uusi esine.

Varmista, että uusi ominaisuus toimii yhdessä olemassa olevan pelin kanssa.

Voit esimerkiksi lisätä:

- uuden vihollisen, jolla on enemmän terveyttä
- uuden kauppatuotteen
- uuden löydettävän esineen
- uuden vaihtoehdon päävalikkoon

## Bonus

Kehitä pelistä laajempi seikkailu.

Voit lisätä esimerkiksi:

- kokemuspisteet ja tasot
- useita alueita
- pomovihollisen
- erilaisia aseita
- avaimella avattavan oven
- useita loppuratkaisuja
- oman taistelujärjestelmän

Voit myös parantaa tallennusta niin, että peli tallentaa esimerkiksi pelaajan sijainnin ja tehdyt tehtävät.

## Lopputyö – oma seikkailupeli

Tee pelistä oma versiosi.

Valitse teema, esimerkiksi:

- fantasiaseikkailu
- avaruusseikkailu
- zombipeli
- aarteenetsintä
- rikosmysteeri
- kauhupeli

Muuta vähintään pelin tarinaa, hahmoja, vihollisia ja esineitä.

Tärkeintä ei ole tehdä mahdollisimman suurta peliä. Tärkeintä on, että ymmärrät, miten eri osat toimivat yhdessä ja osaat muuttaa niitä itse.

## Mitä opit koko kurssilla?

Kurssin aikana opit käyttämään:

- `print()` ja `input()`
- muuttujia
- ehtoja
- `while`- ja `for`-silmukoita
- listoja ja sanakirjoja
- funktioita
- tiedostojen lukemista ja kirjoittamista

Ennen kaikkea opit rakentamaan ohjelmaa vaiheittain.

```text
valmis ohjelma
      ↓
    kokeile
      ↓
    muuta
      ↓
    riko
      ↓
    korjaa
      ↓
    ymmärrä
      ↓
rakenna oma peli
```

**Onneksi olkoon!** Olet käynyt läpi Pythonin perusteet rakentamalla oikean, laajennettavan peliprojektin.

Seuraava askel on jatkaa oman pelisi kehittämistä ja kokeilla, mitä kaikkea osaat rakentaa.