# Osa 3 – Syöte

Osassa 02 peliin lisättiin pelaajan nimi, terveys ja kulta muuttujina.

Nyt pelaaja saa itse antaa nimensä.

## Tavoite

Opit:

* käyttämään `input()`-komentoa
* tallentamaan käyttäjän antaman tiedon muuttujaan
* käyttämään käyttäjän antamaa tietoa pelissä

## Kokeile

Käynnistä `main.py`.

Ohjelma kysyy:

```text
Mikä on nimesi?
```

Kirjoita oma nimesi ja paina Enter.

Huomaa, että nimi näkyy myöhemmin pelissä.

## Tutki

Osassa 02 nimi annettiin suoraan ohjelmakoodissa:

```python
player_name = "Seikkailija"
```

Nyt nimi kysytään pelaajalta:

```python
player_name = input("Mikä on nimesi? ")
```

Jos pelaaja kirjoittaa:

```text
Riku
```

muuttujan arvo on:

```text
player_name → "Riku"
```

Ohjelma voi käyttää tätä tietoa myöhemmin:

```python
print(player_name, "on valmis seikkailuun.")
```

## Muokkaa

Muuta kysymystä.

Esimerkiksi:

```python
player_name = input("Anna sankarisi nimi: ")
```

Muuta myös ohjelman tekstiä niin, että pelaajan nimi esiintyy tarinassa.

## Haaste

Lisää peliin pelaajan **hahmoluokka**.

Kysy esimerkiksi:

```python
character_class = input("Oletko soturi, velho vai varas? ")
```

Tulosta hahmoluokka myöhemmin pelissä:

```python
print("Olet", character_class)
```

Kokeile käyttää tietoa osana tarinaa:

```python
print(player_name, "on", character_class, "ja saapuu metsään.")
```

Tärkeää on, että pelaajan antama tieto **tallennetaan muuttujaan ja sitä käytetään myöhemmin pelissä**.

## Bonus

Käytä pelaajan nimeä useammassa kohdassa pelin tarinaa.

Esimerkiksi:

```python
print(player_name, "katsoo ympärilleen.")
print(player_name, "kuulee metsästä äänen.")
```

Muuta tekstejä niin, että pelaaja tuntuu olevan osa tarinaa.

## Mitä opit?

Ohjelma ei enää pelkästään kerro tarinaa.

Nyt pelaaja voi antaa ohjelmalle tietoa, jota peli käyttää myöhemmin.

```text
pelaaja
   ↓
input()
   ↓
muuttuja
   ↓
peli käyttää tietoa
```

Seuraavassa vaiheessa opitaan tekemään tiedolla jotain vielä kiinnostavampaa: **pelaaja voi tehdä valintoja, jotka vaikuttavat siihen, mitä pelissä tapahtuu.**

## Tarkista

Osaatko:

* käyttää `input()`-komentoa?
* tallentaa vastauksen muuttujaan?
* käyttää muuttujaa myöhemmin pelissä?
* lisätä peliin uuden pelaajan antaman tiedon?

Jos kyllä, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [04 – Ehdot](../04_ehdot/)