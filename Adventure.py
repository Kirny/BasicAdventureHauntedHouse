global key2
key2 = False
from sys import exit

def Start():
	print "Your car breaks down in the middle of the road."
	print "You decide to go to a big house on the side of the street for help"
	print "You encounter a door with a 4 digit lock on it. There is a note attached to the door"
	print "The note reads, the first two digits add up to 8 but when multiplied give the highest value. "
	print "The last part reads, 'July 4th 17XX'"
	decision = raw_input("Should you try to get in the house? Y/N")
	if decision == "Y":
		puzzle1()
	else:
		print "You walk away, eventually you find a person willing to take you to a nearby gas station to call for help"
	
def puzzle1():
	answer1 = raw_input("What four numbers should you try?")
	while answer1 != "4476":
		print "You type the letters in but it gives a weird buzz sound"
		answer1 = raw_input("> ")
	print "The lock clicks and you open the door"
	foyer()
	
def foyer():
	print "There stands a grand foyer. There's a way to the left, and some stairs to the right."
	while True:
		yougo = raw_input("Which way do you go? Right or Left?")
		if yougo == "Right":
			kitchen()
		if yougo == "Left":
			stairhallway()
		else:
			print "That's not a direction."
			
def kitchen():
	key1 = False
	print "You arrive in a nice kitchen. There's not much of interest"
	print "You see a huge sack of flour, a can of beans, and a creaking shaking refridgerator."
	while True:
		investigation = raw_input("Press 1 (investigate flour) 2 (can of beans) 3 (refridgerator) 4 (leave the room)")
		if investigation == "1":
			print "You move the flour and reveal a door?"
			print "Now you can type 'door' to go to this new area"
		if investigation == "2":
			key1 = True
			print "Oh lala there's a key in here... slimey too."
		if investigation == "3":
			refridgerator()
		if investigation == "4":
			foyer()
		if investigation == "door":
			if key1 == True:
				storeroom()
			if key1 == False:
				print "Door is locked"
		else:
			"Huh?"
			
def refridgerator():
	print "You open the refridgerator and suddenly you fall in. You don't know where you are and it..looks...like..you're..de........."
	print "game over."
	exit(0)
	
def storeroom():
	print "Ah, it's dusty in here... better just grab that key I see over there and get the heck out.... *Obtained key!*"
	global key2
	key2 = True
	kitchen()
	
def stairhallway():
	print "You go up the stairs and find 3 rooms...?"
	print "Should you try the first door or the second door? *type first or second or leave*"
	while True:
		whichdoor = raw_input("> ")
		if whichdoor == "first":
			if key2 == False:
				print "wha.. it's locked?"
			if key2 == True:
				treasure()
		if whichdoor == "second":
			print "you touch the knob and suddenly the door screams, this is an easter egg."
		if whichdoor == "step":
			print "You unlock the second door. Congratulations...!?!?! Sorry nothing is programmed here really noone is supposed to come here.."
		if whichdoor == "leave":
			foyer()
		else:
			print "What?"

def treasure():
	print "You open the door and suddenly you see riches beyond your wildest dreams.."
	print "You can't believe it and you're crying so hard.."
	print "You become the next bill gates and your life is handed to you. THE END."
	exit(0)
	
Start()
