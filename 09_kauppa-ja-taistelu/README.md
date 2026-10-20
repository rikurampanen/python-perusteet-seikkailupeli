# Osa 9 – Kauppa ja taistelu

Osassa 08 pelaajan ja vihollisen tiedot koottiin sanakirjoihin.

Nyt nämä tiedot alkavat vaikuttaa pelin tapahtumiin.

Pelaaja voi ostaa terveysjuomia, käyttää niitä taistelussa ja taistella metsäsutta vastaan.

## Tavoite

Opit yhdistämään aikaisemmin opittuja asioita toimivaksi pelimekaniikaksi.

Tässä osassa kertaat:

- muuttujat ja sanakirjat
- ehdot ja silmukat
- listat
- funktiot
- pelaajan terveyden ja kullan muuttaminen
- inventaarion tarkistaminen ja esineen poistaminen

## Kokeile

Avaa tämän kansion `main.py` ja käynnistä ohjelma.

Kokeile seuraavia asioita:

1. Tutki ympäristöä ja kerää köysi.
2. Katso pelaajan tiedot ja inventaario.
3. Mene kauppaan ja osta terveysjuoma.
4. Taistele metsäsutta vastaan.
5. Kokeile käyttää terveysjuomaa taistelussa.
6. Voita vihollinen ja tarkista, paljonko kultaa sait.

Kokeile myös taistelua ilman terveysjuomaa.

## Tutki

### 1. Kaupassa käytetään kultaa

Kaupan funktiossa tarkistetaan ensin, onko pelaajalla tarpeeksi kultaa:

```python
if player["gold"] >= 10:
    player["gold"] -= 10
    inventory.append("terveysjuoma")
```

Jos kultaa on vähintään 10, pelaaja voi ostaa juoman.

Operaattori `-=` vähentää arvosta määrän. Esimerkiksi:

```python
gold = 20
gold -= 10
```

Tämän jälkeen `gold` sisältää arvon `10`.

Oston jälkeen juoma lisätään inventaarioon.

### 2. Taistelu käyttää silmukkaa

Taistelu jatkuu niin kauan kuin pelaaja ja vihollinen ovat elossa:

```python
while player["health"] > 0 and enemy["health"] > 0:
```

Operaattori `and` tarkoittaa, että molempien ehtojen täytyy olla tosia.

Jos pelaajan tai vihollisen terveys putoaa nollaan tai sen alle, taistelusilmukka päättyy.

### 3. Hyökkäys vähentää terveyttä

Pelaajan hyökkäys:

```python
enemy["health"] -= 15
```

Vihollisen hyökkäys:

```python
player["health"] -= enemy["damage"]
```

Koska vihollisen hyökkäysvoima on tallennettu sanakirjaan, samaa koodia voidaan käyttää myös silloin, kun vihollisen hyökkäysvoima muuttuu.

### 4. Terveysjuoman käyttäminen

Ensin peli tarkistaa, onko juoma inventaariossa:

```python
if "terveysjuoma" in inventory:
```

Jos juoma löytyy, se poistetaan listasta:

```python
inventory.remove("terveysjuoma")
```

Tämän jälkeen pelaajan terveyttä lisätään.

Juoma ei kuitenkaan voi nostaa terveyttä yli sadan pisteen.

### 5. Voitosta saa kultaa

Kun vihollisen terveys putoaa nollaan tai sen alle, pelaaja voittaa ja saa kultaa:

```python
if enemy["health"] <= 0:
    player["gold"] += 15
```

Kulta on nyt aidosti hyödyllistä: sitä voi käyttää kaupassa.

## Muokkaa

Kokeile muuttaa pelin tasapainoa.

Muuta esimerkiksi:

- terveysjuoman hintaa
- terveysjuoman palauttamien pisteiden määrää
- pelaajan hyökkäysvoimaa
- vihollisen terveyttä
- vihollisen hyökkäysvoimaa
- taistelusta saatavaa kultapalkkiota

Kokeile muuttaa vain yhtä arvoa kerrallaan. Näin huomaat helpommin, miten se vaikuttaa peliin.

## Haaste

Lisää kauppaan uusi tuote, esimerkiksi toinen terveysjuoma tai taikajuoma.

Päätä:

- tuotteen nimi
- hinta
- mitä tuote tekee
- miten pelaaja voi käyttää sitä

Varmista, ettei pelaaja voi ostaa tuotetta, jos hänellä ei ole tarpeeksi kultaa.

## Bonus

Lisää peliin toinen vihollinen, jolla on eri terveys ja hyökkäysvoima.

Voit myös keksiä taisteluun uuden toiminnon, kuten puolustautumisen, joka vähentää seuraavan vihollishyökkäyksen vahinkoa.

## Mitä opit?

Nyt pelin eri osat vaikuttavat toisiinsa.

```text
kauppa
  ↓
kulta vähenee
  ↓
esine lisätään inventaarioon
  ↓
esine käytetään taistelussa
  ↓
pelaajan terveys muuttuu
  ↓
voitto tuo lisää kultaa
```

Aiemmin opitut muuttujat, ehdot, silmukat, listat, sanakirjat ja funktiot muodostavat nyt yhdessä pelimekaniikan.

## Tarkista

Osaatko:

- vähentää ja lisätä pelaajan kultaa?
- muuttaa pelaajan ja vihollisen terveyttä?
- tarkistaa, onko esine inventaariossa?
- poistaa käytetyn esineen listasta?
- selittää, miksi taistelu käyttää `while`-silmukkaa?
- muuttaa pelin tasapainoa koodia muokkaamalla?

Jos osaat, olet valmis viimeiseen vaiheeseen.

**Seuraavaksi:** [10 – Tallennus ja oma peli](../10_tallennus-ja-oma-peli/)