player_name = input("Mikä on nimesi? ")

health = 100
gold = 20

print()

print("Olet saapunut pimeään metsään.")
print("Aurinko on laskemassa.")
print("Edessäsi on vanha polku.")
print("Polku johtaa syvemmälle metsään.")
print("Lähdet seuraamaan polkua.")
print("Seikkailusi alkaa!")

print()

choice = input("Valitsetko vasemman vai oikean polun? ")

print()

if choice == "vasen":
    print(player_name, "valitsee vasemman polun.")
    print("Polku johtaa pienen puron luokse.")

elif choice == "oikea":
    print(player_name, "valitsee oikean polun.")
    print("Polku johtaa vanhan kivimuurin luokse.")

else:
    print("Et osannut päättää.")
    print("Jäät seisomaan polkujen risteykseen.")

print()

while True:
    print("Mitä haluat tehdä?")
    print("1 - Tutki ympäristöä")
    print("2 - Jatka matkaa")
    print("3 - Lopeta peli")

    action = input("Valitse toiminto: ")

    print()

    if action == "1":
        print("Katselet ympärillesi.")
        print("Metsä näyttää hiljaiselta.")

    elif action == "2":
        print(player_name, "jatkaa matkaa metsässä.")
        print("Polku jatkuu syvemmälle metsään.")

    elif action == "3":
        print("Seikkailu päättyy.")
        break

    else:
        print("Tuntematon valinta.")

    print()