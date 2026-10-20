# Osa 8 – Pelaaja ja viholliset

Osassa 07 jaoimme peliä funktioihin. Nyt jatkamme samaa ohjelmaa ja opettelemme tallentamaan pelaajan ja vihollisten tiedot sanakirjoihin.

Aiemmin pelaajan tiedot olivat erillisissä muuttujissa. Nyt kokoamme ne yhteen rakenteeseen.

## Tavoite

Opit:

- mikä sanakirja on
- miten sanakirja luodaan
- mitä avain ja arvo tarkoittavat
- miten sanakirjasta luetaan tietoja
- miten sanakirjan tietoja käytetään funktioissa

## Kokeile

Avaa tämän kansion `main.py` ja käynnistä ohjelma.

Kokeile valikosta:

1. Katso pelaajan tiedot.
2. Tarkastele vihollista.
3. Kerää köysi tai avain.
4. Katso inventaario.
5. Muuta koodista pelaajan tai vihollisen tietoja ja käynnistä ohjelma uudelleen.

Huomaa, että pelaajan tiedot ja vihollisen tiedot on koottu omiin sanakirjoihinsa.

## Tutki

### 1. Pelaajan tiedot sanakirjassa

Ohjelmassa on:

```python
player = {
    "name": player_name,
    "health": 100,
    "gold": 20
}
```

Sanakirja tallentaa tietoja avain-arvo-pareina.

| Avain | Arvo |
|---|---|
| `"name"` | Pelaajan nimi |
| `"health"` | Terveys |
| `"gold"` | Kulta |

Avain kertoo, mitä tietoa ollaan käsittelemässä. Arvo on itse tallennettu tieto.

### 2. Tietojen lukeminen

Pelaajan terveys saadaan näin:

```python
player["health"]
```

Pelaajan nimi saadaan näin:

```python
player["name"]
```

Näitä tietoja voidaan käyttää myös tulostuksessa:

```python
print("Terveys:", player["health"])
```

Huomaa, että sanakirjan avain kirjoitetaan hakasulkeisiin.

### 3. Vihollisen tiedot

Vihollinen tallennetaan omaan sanakirjaansa:

```python
enemy = {
    "name": "Metsäsusi",
    "health": 30,
    "damage": 10
}
```

Sanakirjaan tallennetaan vihollisen nimi, terveys ja hyökkäysvoima.

Näin jokaisella hahmolla voi olla omat tietonsa.

Myöhemmin terveys voi vähentyä taistelussa ja hyökkäysvoimaa voidaan käyttää vahingon laskemiseen.

### 4. Sanakirja ja funktio

Aiemmin pelaajan tietoja käsiteltiin useilla erillisillä arvoilla.

Nyt funktiolle annetaan koko sanakirja:

```python
def show_player_status(player):
    print("Pelaaja:", player["name"])
    print("Terveys:", player["health"])
    print("Kulta:", player["gold"])
```

Funktiota kutsutaan näin:

```python
show_player_status(player)
```

Funktio saa käyttöönsä pelaajan sanakirjan ja lukee siitä tarvittavat tiedot.

## Muokkaa

Muuta pelaajan tietoja:

```python
player = {
    "name": player_name,
    "health": 80,
    "gold": 50
}
```

Muuta myös vihollisen tietoja:

```python
enemy = {
    "name": "Luolapeikko",
    "health": 60,
    "damage": 15
}
```

Käynnistä ohjelma ja tarkastele tuloksia.

## Haaste

Lisää vihollisen sanakirjaan uusi avain:

```python
"location": "Pimeä metsä"
```

Muokkaa sen jälkeen `show_enemy`-funktiota niin, että se tulostaa myös vihollisen sijainnin.

Kokeile lisätä viholliselle myös jokin muu tieto, kuten `"type"` tai `"gold_reward"`.

## Bonus

Lisää toinen vihollinen omaan sanakirjaansa.

Anna sille eri nimi, terveys ja hyökkäysvoima.

Muuta valikkoa niin, että pelaaja voi valita, kumman vihollisen tietoja hän tarkastelee.

## Mitä opit?

Sanakirjan avulla saman hahmon tiedot pysyvät yhdessä paikassa.

```text
player
  ├── name
  ├── health
  └── gold

enemy
  ├── name
  ├── health
  └── damage
```

Funktiot voivat käsitellä sanakirjoja, joten ohjelman eri osat voivat käyttää samoja tietoja.

## Tarkista

Osaatko:

- luoda sanakirjan?
- selittää avaimen ja arvon eron?
- lukea arvon esimerkiksi komennolla `player["health"]`?
- antaa sanakirjan parametrina funktiolle?
- lisätä sanakirjaan uuden tiedon?

Jos osaat, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [09 – Kauppa ja taistelu](../09_kauppa-ja-taistelu/)