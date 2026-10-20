# Osa 6 – Inventaario

Osassa 05 peliin lisättiin toistuva pelivalikko.

Nyt pelaaja voi alkaa kerätä esineitä.

Tällä kertaa emme muuta aikaisempia toimintoja.

Lisäämme niiden päälle uuden ominaisuuden: **inventaarion**.

## Tavoite

Pelaaja voi:

* tutkia ympäristöä
* löytää esineen
* ottaa esineen mukaan
* katsoa inventaariota
* jatkaa matkaa
* lopettaa pelin

Opit:

* listat
* `.append()`
* `for`-silmukan
* listan läpikäymisen

## Kokeile

Käynnistä `main.py`.

Valikossa on nyt:

```text
1 - Tutki ympäristöä
2 - Ota köysi
3 - Jatka matkaa
4 - Katso inventaario
5 - Lopeta peli
```

Valitse ensin:

```text
1
```

Pelaaja tutkii ympäristöä.

Huomaa, että toiminta on sama kuin osassa 05:

```text
Katselet ympärillesi.
Metsä näyttää hiljaiselta.
```

Sen jälkeen valitse:

```text
2
```

Pelaaja ottaa köyden mukaansa.

Lopuksi valitse:

```text
4
```

Köysi näkyy inventaariossa.

## Tutki

Inventaario luodaan ohjelman alussa:

```python
inventory = []
```

Aluksi lista on tyhjä.

Kun pelaaja ottaa köyden, se lisätään listaan:

```python
inventory.append("köysi")
```

Nyt inventaario sisältää:

```text
["köysi"]
```

`.append()` tarkoittaa, että listan loppuun lisätään uusi asia.

## Inventaarion näyttäminen

Inventaarion sisältö voidaan käydä läpi `for`-silmukalla:

```python
for item in inventory:
    print("-", item)
```

Jos inventaariossa on:

```text
["köysi"]
```

ohjelma näyttää:

```text
- köysi
```

Jos myöhemmin inventaarioon lisätään muita esineitä:

```text
["köysi", "kartta", "avain"]
```

`for` käy kaikki esineet läpi yksi kerrallaan.

## Muokkaa

Lisää peliin toinen esine.

Voit esimerkiksi lisätä uuden toiminnon:

```text
6 - Ota kartta
```

Kun pelaaja valitsee sen, lisää kartta inventaarioon:

```python
inventory.append("kartta")
```

Muista lisätä myös kartta inventaarion näyttämiseen.

## Haaste

Lisää peliin uusi esine, jonka pelaaja voi ottaa mukaansa.

Voit esimerkiksi käyttää:

* karttaa
* taskulamppua
* avainta
* miekkaa
* juomapulloa

Lisää sille oma valikkovaihtoehto.

Esimerkiksi:

```text
6 - Ota kartta
```

Kun pelaaja valitsee vaihtoehdon, esine lisätään inventaarioon.

Tarkista lopuksi inventaariosta, että esine todella tallentui listaan.

## Bonus

Muuta tutkimista niin, että pelaaja löytää jotain uutta.

Esimerkiksi:

```text
Katselet ympärillesi.
Metsä näyttää hiljaiselta.
Huomaat kauempana vanhan arkun.
```

Älä kuitenkaan lisää arkkua vielä automaattisesti inventaarioon.

Pelaajan pitää itse päättää, mitä hän ottaa mukaansa.

## Mitä opit?

Nyt pelissä on ensimmäinen paikka, johon pelaajan tavaroita voidaan tallentaa.

```text
pelaaja
   ↓
löytää esineen
   ↓
ottaa esineen
   ↓
inventory.append()
   ↓
esine tallentuu inventaarioon
```

Aikaisempaa peliä ei poistettu.

Sen sijaan siihen lisättiin uusi ominaisuus.

```text
Osa 05
↓
pelivalikko

Osa 06
↓
pelivalikko
+
inventaario
```

Tätä samaa ajatusta käytetään koko loppukurssin ajan.

Uutta rakennetaan aina aikaisemman pelin päälle.

## Tarkista

Osaatko:

* luoda listan?
* lisätä listaan `.append()`-komennolla?
* käyttää `for`-silmukkaa listan läpikäymiseen?
* tehdä toiminnon, joka lisää esineen inventaarioon?
* näyttää inventaarion pelaajalle?

Jos kyllä, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [07 – Funktiot](../07_funktiot/)