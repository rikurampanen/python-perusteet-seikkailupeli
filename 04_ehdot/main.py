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

print("Edessäsi polku haarautuu kahteen suuntaan.")
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

print("Pelaaja:", player_name)
print("Terveys:", health)
print("Kulta:", gold)