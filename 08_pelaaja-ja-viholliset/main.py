def show_player_status(player):
    print("Pelaaja:", player["name"])
    print("Terveys:", player["health"])
    print("Kulta:", player["gold"])


def show_inventory(inventory):
    print("Inventaario:")

    if len(inventory) == 0:
        print("Inventaario on tyhjä.")
    else:
        for item in inventory:
            print("-", item)


def show_enemy(enemy):
    print("Vihollinen:", enemy["name"])
    print("Terveys:", enemy["health"])
    print("Hyökkäysvoima:", enemy["damage"])


player_name = input("Mikä on nimesi? ")

player = {
    "name": player_name,
    "health": 100,
    "gold": 20
}

enemy = {
    "name": "Metsäsusi",
    "health": 30,
    "damage": 10
}

inventory = []

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
    print(player["name"], "valitsee vasemman polun.")
    print("Polku johtaa pienen puron luokse.")

elif choice == "oikea":
    print(player["name"], "valitsee oikean polun.")
    print("Polku johtaa vanhan kivimuurin luokse.")

else:
    print("Et osannut päättää.")
    print("Jäät seisomaan polkujen risteykseen.")

print()

while True:
    print("Mitä haluat tehdä?")
    print("1 - Tutki ympäristöä")
    print("2 - Jatka matkaa")
    print("3 - Katso inventaario")
    print("4 - Katso pelaajan tiedot")
    print("5 - Tarkastele vihollista")
    print("6 - Lopeta peli")

    action = input("Valitse toiminto: ")

    print()

    if action == "1":
        print("Katselet ympärillesi.")
        print("Metsä näyttää hiljaiselta.")

        if "köysi" not in inventory:
            print("Huomaat maassa vanhan köyden.")

            item_choice = input(
                "Otatko köyden mukaasi? (kyllä/ei) "
            )

            if item_choice == "kyllä":
                inventory.append("köysi")
                print("Otat köyden mukaasi.")
            else:
                print("Jätät köyden maahan.")

        else:
            print("Et löydä enää mitään uutta.")

    elif action == "2":
        print(player["name"], "jatkaa matkaa metsässä.")
        print("Polku jatkuu syvemmälle metsään.")

        if "avain" not in inventory:
            print("Polun vieressä huomaat jotain kiiltävää.")
            print("Löydät vanhan avaimen.")

            item_choice = input(
                "Otatko avaimen mukaasi? (kyllä/ei) "
            )

            if item_choice == "kyllä":
                inventory.append("avain")
                print("Otat avaimen mukaasi.")
            else:
                print("Jätät avaimen maahan.")

        else:
            print("Polun varrella ei ole enää mitään uutta.")

    elif action == "3":
        show_inventory(inventory)

    elif action == "4":
        show_player_status(player)

    elif action == "5":
        show_enemy(enemy)

    elif action == "6":
        print("Seikkailu päättyy.")
        break

    else:
        print("Tuntematon valinta.")

    print()