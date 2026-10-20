import json


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


def save_game(player, enemy, inventory):
    game_data = {
        "player": player,
        "enemy": enemy,
        "inventory": inventory
    }

    with open("save.json", "w", encoding="utf-8") as file:
        json.dump(game_data, file, ensure_ascii=False, indent=4)

    print("Peli tallennettu!")


def load_game():
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            game_data = json.load(file)

        print("Tallennettu peli löytyi.")
        return game_data

    except FileNotFoundError:
        print("Tallennettua peliä ei löytynyt.")
        return None

    except json.JSONDecodeError:
        print("Tallennustiedosto ei ole kelvollinen.")
        return None


def visit_shop(player, inventory):
    print("Saavut pieneen kauppaan.")
    print("1 - Terveysjuoma (10 kultaa)")
    print("2 - Poistu kaupasta")

    choice = input("Mitä haluat tehdä? ")

    if choice == "1":
        if player["gold"] >= 10:
            player["gold"] -= 10
            inventory.append("terveysjuoma")
            print("Ostit terveysjuoman.")
            print("Kultaa jäljellä:", player["gold"])
        else:
            print("Sinulla ei ole tarpeeksi kultaa.")

    elif choice == "2":
        print("Poistut kaupasta.")

    else:
        print("Tuntematon valinta.")


def battle(player, enemy, inventory):
    if enemy["health"] <= 0:
        print("Olet jo voittanut tämän vihollisen.")
        return

    print("Taistelu alkaa!")
    print("Vastassasi on", enemy["name"] + ".")

    while player["health"] > 0 and enemy["health"] > 0:
        print()
        print("Oma terveys:", player["health"])
        print("Vihollisen terveys:", enemy["health"])
        print("1 - Hyökkää")
        print("2 - Käytä terveysjuoma")
        print("3 - Pakene")

        choice = input("Valitse toiminto: ")

        print()

        if choice == "1":
            enemy["health"] -= 15
            print("Hyökkäät vihollisen kimppuun!")

            if enemy["health"] > 0:
                player["health"] -= enemy["damage"]
                print("Vihollinen hyökkää takaisin!")
                print("Menetät", enemy["damage"], "terveyspistettä.")

        elif choice == "2":
            if "terveysjuoma" in inventory:
                inventory.remove("terveysjuoma")

                player["health"] = min(
                    player["health"] + 30, 100
                )

                print("Käytät terveysjuoman.")
                print("Terveys:", player["health"])

                if enemy["health"] > 0:
                    player["health"] -= enemy["damage"]
                    print("Vihollinen hyökkää!")
                    print("Menetät", enemy["damage"],
                          "terveyspistettä.")
            else:
                print("Sinulla ei ole terveysjuomaa.")

        elif choice == "3":
            print("Pakenet taistelusta.")
            break

        else:
            print("Tuntematon valinta.")

    print()

    if enemy["health"] <= 0:
        print("Voitit taistelun!")
        print("Saat palkkioksi 15 kultaa.")
        player["gold"] += 15

    elif player["health"] <= 0:
        print("Terveys loppui. Seikkailusi on päättynyt.")


# Ladataan aiempi peli tai aloitetaan uusi.

saved_game = load_game()

if saved_game is not None:
    choice = input("Jatketaanko tallennettua peliä? (kyllä/ei) ")

else:
    choice = "ei"

if choice == "kyllä":
    player = saved_game["player"]
    enemy = saved_game["enemy"]
    inventory = saved_game["inventory"]

    print("Tervetuloa takaisin,", player["name"] + "!")

else:
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
    print("Seikkailusi alkaa!")

    print()

    path = input("Valitsetko vasemman vai oikean polun? ")

    if path == "vasen":
        print("Polku johtaa pienen puron luokse.")
    elif path == "oikea":
        print("Polku johtaa vanhan kivimuurin luokse.")
    else:
        print("Jäät seisomaan polkujen risteykseen.")

print()

while True:
    if player["health"] <= 0:
        print("Peli päättyy, koska terveytesi loppui.")
        break

    print("Mitä haluat tehdä?")
    print("1 - Tutki ympäristöä")
    print("2 - Jatka matkaa")
    print("3 - Katso inventaario")
    print("4 - Katso pelaajan tiedot")
    print("5 - Mene kauppaan")
    print("6 - Taistele metsäsutta vastaan")
    print("7 - Tallenna peli")
    print("8 - Lopeta peli")

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
        visit_shop(player, inventory)

    elif action == "6":
        battle(player, enemy, inventory)

    elif action == "7":
        save_game(player, enemy, inventory)

    elif action == "8":
        print("Seikkailu päättyy.")
        break

    else:
        print("Tuntematon valinta.")

    print()