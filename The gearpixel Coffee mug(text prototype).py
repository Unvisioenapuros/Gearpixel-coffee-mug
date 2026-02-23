while True:
	#print statements
	print("Coffee mug is empty.")

	#Random generator for doppio
	import random

	#Ingridient list
	ingridients_list = {
	"Coffee":False,
	"Milk":False,
	"Water":False,
	"Ice":False
	}

	#Add ingridents
	for item in ingridients_list:
		while True:
			print(f"Add {item}?[y/n]?")
			ingridient = input()
			if ingridient=="y":
				ingridients_list[item] = True
				break
			elif ingridient=="n":
				break
			else:
				print("¡Opción invalida!")


	#Recipe dictionary
	state = (
		ingridients_list["Coffee"],
    ingridients_list["Milk"],
    ingridients_list["Water"]
    )

	recipes = {
		(False, False, False): "Nothing" ,
		(True, False, False): "Coffee" ,
		(False, True, False): "Hot milk" ,
		(False, False, True): "Water",
		(True, True, False): "Coffee & milk",
		(True, False, True): "Americano" ,
		(False, True, True): "Diluted milk" ,
		(True, True, True): "Diluted, coffee & milk"
	}

	description = {
		(False, False, False): "Why did you do this?" ,
		(True, False, False): "Pure caffeine packed into a shot, some baristas might make you a Doppio if you ask nicely." ,
		(False, True, False): "This nice bevarage can put anyone to sleep." ,
		(False, False, True): "Cold and refreshing! Perfect for the summer",
		(True, True, False): "Children always want coffee yet don't like the taste. This bevarage is perfect for them!",
		(True, False, True): "This is coffee... but less flavorfull." ,
		(False, True, True): "Ran out of milk? Don't worry! Just add some water, no one will feel the difference." ,
		(True, True, True): "This bevarage with even less coffee flavour is perfect for children."
	}

	base_drink = recipes[state]

	if base_drink == "Coffee":
		final_drink = random.choice([
		"Espresso",
		"Espresso",
		"Espresso",
		"Espresso",
		"Espresso",
		"Espresso",
		"Espresso",
		"Espresso",
		"Espresso",
		"Doppio"
		])
	else:
		final_drink = base_drink

	final_drink_description = description[state]

	if ingridients_list["Ice"] and final_drink == "Hot milk":
		final_drink = "Milk"
		final_drink_description = "Just milk, perfect for babies and toddlers."
	elif ingridients_list["Ice"] and final_drink == "Diluted, coffee & milk":
		final_drink = "Frapuccino"
		final_drink_description = "Stolen directly from Starbucks"
	elif ingridients_list["Ice"] and final_drink == "Nothing":
		final_drink = "Ice"
		final_drink_description = "It's just ice, are you waiting for it to melt to become water?"
	elif ingridients_list["Ice"] and final_drink not in ("Hot milk", "Nothing", "Diluted, coffee & milk"):
		final_drink = final_drink.lower()
		final_drink = "Iced " + final_drink

	print(final_drink)
	print(final_drink_description)

	print("Play again [y/n]?")
	play = input()
	if play=="y":
		continue
	else:
		break