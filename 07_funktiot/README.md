# Osa 7 – Funktiot

Osassa 06 peliin lisättiin inventaario, johon pelaaja voi kerätä esineitä.

Nyt jatkamme samaa peliä ja opettelemme jakamaan koodia pienempiin osiin **funktioiden avulla**.

## Tavoite

Opit:

- mikä funktio on
- miten funktio määritellään `def`-komennolla
- miten funktiota kutsutaan
- mitä parametrit tarkoittavat
- miten samaa funktiota voi käyttää useita kertoja

## Kokeile

Avaa tämän kansion `main.py` ja käynnistä ohjelma.

Kokeile valikosta:

- tutkia ympäristöä
- kerätä esineitä
- katsoa inventaario
- katsoa pelaajan tiedot

Huomaa, että pelaajan tiedot ja inventaario tulostetaan funktioiden avulla.

## Tutki

### 1. Funktion määrittely

Ohjelman alussa on:

```python
def show_inventory(inventory):
    print("Inventaario:")

    if len(inventory) == 0:
        print("Inventaario on tyhjä.")
    else:
        for item in inventory:
            print("-", item)
```

`def` aloittaa funktion määrittelyn.

`show_inventory` on funktion nimi.

Suluissa oleva `inventory` on parametri. Sen avulla funktio saa käyttöönsä listan, jonka sisältö tulostetaan.

Sisennetyt rivit kuuluvat funktion sisälle.

### 2. Funktion kutsuminen

Pelkkä funktion määrittely ei vielä suorita sen sisältöä.

Funktiota kutsutaan näin:

```python
show_inventory(inventory)
```

Tämä suorittaa funktion ja antaa sille pelin inventaarion.

Pelaajan tietojen tulostamiseen käytetään toista funktiota:

```python
show_player_status(player_name, health, gold)
```

Sama funktio voidaan kutsua aina, kun pelaajan tiedot halutaan näyttää.

### 3. Parametrit

Funktion määrittelyssä:

```python
def show_player_status(player_name, health, gold):
```

funktio saa kolme parametria:

- `player_name`
- `health`
- `gold`

Niiden avulla funktio voi tulostaa juuri kyseisen pelaajan tiedot.

## Muokkaa

Muuta `show_player_status`-funktion tulostamia tekstejä.

Voit esimerkiksi tulostaa:

```python
print(player_name, "on valmis seikkailuun!")
```

Kokeile myös lisätä funktioon tieto pelaajan inventaariosta tai muuttaa inventaarion tulostusta.

## Haaste

Tee uusi funktio nimeltä `show_welcome`.

Sen tehtävä on tulostaa pelin aloitustekstit.

Siirrä nämä rivit funktion sisälle:

```python
print("Olet saapunut pimeään metsään.")
print("Aurinko on laskemassa.")
print("Edessäsi on vanha polku.")
print("Polku johtaa syvemmälle metsään.")
print("Lähdet seuraamaan polkua.")
print("Seikkailusi alkaa!")
```

Kutsu funktiota sen jälkeen sopivassa kohdassa ohjelmaa:

```python
show_welcome()
```

Varmista, että aloitustekstit näkyvät edelleen vain kerran.

## Bonus

Tee funktio, joka tulostaa pelin valikon.

Voit nimetä sen esimerkiksi `show_menu`.

Siirrä valikon tulostusrivit funktion sisälle ja kutsu sitä `while`-silmukassa.

## Mitä opit?

Funktio kokoaa yhteen tehtävän, jonka ohjelma voi suorittaa aina tarvittaessa.

```text
funktion määrittely
       ↓
funktion kutsuminen
       ↓
funktio suorittaa tehtävän
```

Funktioiden avulla peliä on helpompi lukea, korjata ja laajentaa.

## Tarkista

Osaatko:

- määritellä funktion `def`-komennolla?
- kutsua funktiota?
- selittää, mitä parametri tarkoittaa?
- siirtää koodia funktion sisälle niin, että ohjelma toimii edelleen?

Jos osaat, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [08 – Pelaaja ja viholliset](../08_pelaaja-ja-viholliset/)