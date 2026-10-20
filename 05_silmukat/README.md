# Osa 5 – Silmukat

Osassa 04 pelaaja pystyi tekemään valinnan, joka vaikutti pelin tapahtumiin.

Nyt peliin lisätään **toistaminen**.

Pelaaja voi liikkua metsässä useamman kerran ilman, että samaa koodia tarvitsee kirjoittaa uudelleen.

## Tavoite

Lisätään peliin pieni pelivalikko.

Pelaaja voi:

* tutkia metsää
* jatkaa matkaa
* lopettaa pelin

Valikko toistuu, kunnes pelaaja päättää lopettaa.

Opit:

* `while`
* toistamisen
* silmukan lopettamisen
* ohjelman kulun hallintaa

## Kokeile

Käynnistä `main.py`.

Kun tarinan alku on pelattu, ohjelma näyttää valikon:

```text
Mitä haluat tehdä?

1 - Tutki ympäristöä
2 - Jatka matkaa
3 - Lopeta peli
```

Valitse esimerkiksi:

```text
1
```

Ohjelma suorittaa toiminnon ja näyttää valikon uudelleen.

Kokeile vaihtoehtoa `2`.

Sen jälkeen kokeile vaihtoehtoa `3`.

Huomaa, että vaihtoehto `1` tai `2` ei lopeta peliä.

Valikko tulee uudelleen näkyviin.

## Tutki

Valikon toistaminen tehdään `while`-silmukalla:

```python
while True:
    choice = input("Valitse toiminto: ")
```

`while` tarkoittaa:

> Toista koodia niin kauan kuin ehto on tosi.

Tässä käytetään:

```python
while True:
```

Se tarkoittaa, että silmukka jatkuu.

Silmukasta voidaan poistua komennolla:

```python
break
```

Esimerkiksi:

```python
if choice == "3":
    print("Seikkailu päättyy.")
    break
```

Kun pelaaja valitsee `3`, `break` lopettaa silmukan.

## Muokkaa

Muuta valikon tekstejä.

Voit esimerkiksi vaihtaa:

```text
1 - Tutki ympäristöä
```

muotoon:

```text
1 - Katso ympärillesi
```

Muuta myös toiminnon tulostamaa tekstiä.

Esimerkiksi:

```python
print("Katselet ympärillesi.")
print("Metsä näyttää hiljaiselta.")
```

Kokeile tehdä valikosta oman pelisi näköinen.

## Haaste

Lisää valikkoon uusi toiminto.

Esimerkiksi:

```text
4 - Lepää
```

Kun pelaaja valitsee `4`, ohjelman pitäisi tulostaa jotain, joka liittyy lepäämiseen.

Esimerkiksi:

```text
Löydät sopivan paikan levätä.
Levähtäessäsi kuulet metsästä oudon äänen.
```

Tärkeää on, että uusi vaihtoehto toimii myös silmukan sisällä.

Kun toiminto on suoritettu, valikon pitäisi tulla uudelleen näkyviin.

## Bonus

Lisää peliin toiminto:

```text
5 - Katso pelaajan tiedot
```

Kun pelaaja valitsee sen, näytä:

* pelaajan nimi
* terveys
* kulta

Voit käyttää jo aikaisemmista osista tuttuja muuttujia:

```python
print("Pelaaja:", player_name)
print("Terveys:", health)
print("Kulta:", gold)
```

Näin aikaisemmin luodut tiedot alkavat saada enemmän käyttöä pelissä.

## Mitä opit?

Aikaisemmin ohjelma eteni kerran alusta loppuun.

Nyt ohjelma voi jäädä odottamaan pelaajaa:

```text
        ↓
    näytä valikko
        ↓
    pelaajan valinta
        ↓
    suorita toiminto
        ↓
    takaisin valikkoon
        ↑
        └────────
```

`while` tekee mahdolliseksi ohjelman toistamisen.

`break` puolestaan antaa meille tavan poistua silmukasta.

Tämä on tärkeä osa pelejä, koska pelin pitää yleensä jatkua niin kauan kuin pelaaja haluaa pelata.

## Tarkista

Osaatko:

* tehdä `while`-silmukan?
* käyttää silmukkaa valikon toistamiseen?
* käyttää `break`-komentoa?
* lisätä uuden toiminnon valikkoon?
* pitää aikaisemmin luodut pelaajan tiedot mukana pelissä?

Jos kyllä, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [06 – Inventaario](../06_inventaario/)