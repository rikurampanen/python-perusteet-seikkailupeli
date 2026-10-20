# Osa 2 – Muuttujat

Osassa 01 teimme ensimmäisen version seikkailupelistä.

Nyt jatkamme **samaa ohjelmaa**.

Tässä osassa opetetaan ohjelma muistamaan pelaajaan liittyviä tietoja muuttujien avulla.

## Tavoite

Lisätään peliin:

* pelaajan nimi
* terveys
* kulta

Opit samalla:

* mikä muuttuja on
* miten muuttuja luodaan
* miten muuttujan arvoa käytetään

## Kokeile

Avaa tämän kansion `main.py` ja käynnistä ohjelma.

Pelin tarina on edelleen sama kuin osassa 01.

Sen lisäksi ohjelma näyttää pelaajan tiedot seikkailun alussa.

## Tutki

Ohjelman alussa on:

```python
player_name = "Seikkailija"
health = 100
gold = 20
```

Näissä kolmessa muuttujassa säilytetään tietoa.

```text
player_name → "Seikkailija"
health      → 100
gold        → 20
```

Muuttujan avulla tietoa voidaan käyttää myöhemmin ohjelmassa.

Esimerkiksi:

```python
print("Pelaaja:", player_name)
```

tulostaa:

```text
Pelaaja: Seikkailija
```

## Muokkaa

Muuta pelaajan nimeä.

Esimerkiksi:

```python
player_name = "Ritari"
```

Muuta myös terveyden ja kullan määrää.

Kokeile esimerkiksi:

```python
health = 80
gold = 50
```

Käynnistä ohjelma uudelleen ja katso, mitä muuttui.

## Haaste

Luo oma hahmosi.

Päätä:

* hahmon nimi
* hahmon terveys
* hahmon kullan määrä

Esimerkiksi:

```python
player_name = "Velho"
health = 70
gold = 40
```

## Bonus

Kokeile muuttaa vain yhtä arvoa ja käynnistä ohjelma uudelleen.

Mitä tapahtuu, jos:

```python
health = 10
```

Entä jos:

```python
gold = 1000
```

Peli ei vielä käytä kultaa tai terveyttä mihinkään.

Se muuttuu myöhemmissä vaiheissa.

## Mitä opit?

Ohjelma voi tallentaa tietoa muuttujiin.

Tässä vaiheessa meillä on:

```text
pelaajan nimi
terveys
kulta
```

Myöhemmin näitä samoja tietoja käytetään oikeasti pelissä.

Esimerkiksi:

* terveys voi vähentyä taistelussa
* kultaa voidaan käyttää kaupassa
* pelaajan nimi voidaan kysyä pelaajalta

## Tarkista

Osaatko:

* selittää, mikä muuttuja on?
* luoda muuttujan?
* muuttaa muuttujan arvoa?
* käyttää muuttujaa `print()`-komennossa?

Jos osaat, olet valmis seuraavaan vaiheeseen.

**Seuraavaksi:** [03 – Syöte](../03_syote/)