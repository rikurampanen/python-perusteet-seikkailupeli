# Osa 4 – Ehdot

Osassa 03 pelaaja sai antaa pelille oman nimensä ja hahmoluokkansa.

Nyt peli alkaa **reagoida pelaajan valintoihin**.

Tässä osassa opitaan ehdot `if`, `elif` ja `else`.

## Tavoite

Lisätään peliin ensimmäinen oikea valinta.

Pelaaja pääsee valitsemaan kahden polun välillä.

Valinta vaikuttaa siihen, mitä pelissä tapahtuu.

Opit:

* `if`
* `elif`
* `else`
* ehtojen käyttämisen ohjelman kulun muuttamiseen
* käyttäjän antaman vastauksen vertaamisen

## Kokeile

Käynnistä `main.py`.

Ohjelma kysyy ensin pelaajan nimen.

Sen jälkeen tarina etenee tuttuun tapaan.

Lopulta pelaaja kohtaa kaksi polkua:

```text
Edessäsi polku haarautuu kahteen suuntaan.
Valitsetko vasemman vai oikean polun?
```

Kokeile kirjoittaa:

```text
vasen
```

Sen jälkeen käynnistä ohjelma uudelleen ja kirjoita:

```text
oikea
```

Huomaa, että tarina muuttuu valinnan mukaan.

## Tutki

Valinta tallennetaan muuttujaan:

```python
choice = input("Valitsetko vasemman vai oikean polun? ")
```

Sen jälkeen ohjelma tarkistaa vastauksen:

```python
if choice == "vasen":
    print(player_name, "valitsee vasemman polun.")
```

Tarkoittaa:

> Jos pelaajan vastaus on `"vasen"`, suorita tämä koodi.

Seuraavaksi:

```python
elif choice == "oikea":
    print(player_name, "valitsee oikean polun.")
```

`elif` tarkoittaa:

> Jos ensimmäinen ehto ei toteutunut, kokeile tätä ehtoa.

Lopuksi:

```python
else:
    print("Et osannut päättää.")
```

`else` suoritetaan silloin, kun mikään aikaisemmista ehdoista ei toteudu.

Esimerkiksi jos pelaaja kirjoittaa:

```text
ylös
```

ohjelma päätyy `else`-kohtaan.

## Muokkaa

Muuta vasemman ja oikean polun tapahtumia.

Esimerkiksi vasemmalla polulla voisi olla:

```python
print("Löydät vanhan sillan.")
```

ja oikealla:

```python
print("Löydät hylätyn leirin.")
```

Kokeile tehdä poluista oman pelisi näköisiä.

## Haaste

Lisää peliin uusi valinta.

Esimerkiksi pelaaja voisi löytää metsästä oven:

```text
Saavut vanhan oven luokse.
Avaatko oven vai jatkatko matkaa?
```

Tallenna vastaus muuttujaan ja käytä `if`-rakennetta päättämään, mitä tapahtuu.

Esimerkiksi:

```python
door_choice = input("Avaatko oven vai jatkatko matkaa? ")
```

Tee vähintään kaksi vaihtoehtoa:

* oven avaaminen
* matkan jatkaminen

Molempien vaihtoehtojen pitää johtaa erilaiseen tapahtumaan.

## Bonus

Tee valinnasta osa tarinaa.

Esimerkiksi jos pelaaja valitsee vasemman polun, hän voisi löytää jotain hyödyllistä.

Jos pelaaja valitsee oikean polun, hän voisi joutua vaaralliseen tilanteeseen.

Älä vielä muuta terveyttä tai kultaa.

Niitä tarvitaan myöhemmin, kun peliin lisätään lisää pelimekaniikkaa.

## Mitä opit?

Ohjelma osaa nyt tehdä päätöksiä.

Aikaisemmin ohjelma eteni aina samalla tavalla:

```text
aloitus
   ↓
metsä
   ↓
polku
   ↓
loppu
```

Nyt pelaajan valinta voi muuttaa ohjelman kulkua:

```text
              ┌→ vasen → tapahtuma A
pelaajan valinta
              └→ oikea → tapahtuma B
```

Tämä on tärkeä askel.

Peli ei enää vain kerro tarinaa, vaan **reagoi pelaajan tekemisiin**.

## Tarkista

Osaatko:

* käyttää `if`-ehtoa?
* käyttää `elif`-ehtoa?
* käyttää `else`-ehtoa?
* verrata muuttujan arvoa esimerkiksi `==`-operaattorilla?
* tehdä valinnan, joka muuttaa pelin tapahtumaa?

Jos kyllä, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [05 – Silmukat](../05_silmukat/)