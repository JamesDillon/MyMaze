################################
# top         top          top #
# west     mid (door)      east#
#   ##########    ##########   #
#   #        #    #        #   #
#   #        #    #        #   #
# m ##########    ##########   #
# west       middle      mid ea#
#   ##########    ##########   #
#   #        #    #        #   #
#   #        #    #        #   #
#   ##########    ##########   #
#           bottom       bottom#
# start       mid         east #
################################

print "You wake up in a maze\n"
print "There's no light... It seems you're going blind!\n"

print "Controls are: \n"
print "North - n"
print "South - s"
print "West - w"
print "East - e\n"

def start():
	print "You're at the bottom left hand corner of the maze\n"
	print "You can only go north and east\n"
	
	while True:
		direction = raw_input("> ")
		if direction == 'n':
			mid_west()
			break
		elif direction == 'e':
			bottom_middle()
			break

def mid_west():
	print "You are north of were you started...\n"
	print "You can go south (back to beginning), east or north.\n"

	while True:
		direction = raw_input("> ")
		if direction == 'n':
			top_west()
			break
		elif direction == 'e':
			middle()
			break
		elif direction == 's':
			start()
			break

def top_west():
	print "You are further north from where you started! (Top left hand corner)\n"
	print "You can go east and south.\n"

	while True:
		direction = raw_input("> ")
		if direction == 'e':
			top_middle()
			break
		elif direction == 's':
			mid_west()
			break

def bottom_middle():
	print "You are east of where you started.\n"
	print "You can go north, west and east.\n"

	while True:
		direction = raw_input("> ")
		if direction == 'n':
			middle()
			break
		elif direction == 'w':
			start()
			break
		elif direction == 'e':
			bottom_east()
			break

def middle():
	print "You are dead center of the map...\n"
	print "You can go west, north, east and south!\n"
	print "\n"
	print "You find a gold statue sitting on a pillar (like indiana jones)."
	print "What do you do: \n"
	print "1. Snatch the statue and run."
	print "2. Quickly replace the statue with a sand bag."
	print "3. Steal the pillar the statue is sitting on... For some reason."

	while True:
		direction = raw_input("> ")
		if direction == 'n':
			top_middle()
			break
		elif direction == 's':
			bottom_middle()
			break
		elif direction == 'e':
			mid_east()
			break
		elif direction == 'w':
			mid_west()
			break
		elif direction == '1':
			print "\n"
			print "This wasn't just an ordinary statue!"
			print "It was a PORTKEY, like that one in harrypotter!"
			print "You were teleported to Richard Stallman's bedroom..."
			print "On closer inspection, his room is littered with dildos\n"
			print "To which you are abruptly beaten to death with one by him."
			break
		elif direction == '2':
			print "\n"
			print "You picked up a sandbag from the floor..."
			print "Little did you know, it wasn't a sandbag.\n"
			print "IT WAS A BAG FILLED WITH SPIDERS!!!"
			print "You hate spiders, and because of this you have a heart attack and die."
			print "Better luck next life..."
			break
		elif direction == '3':
			print "\n"
			print "You steal the concrete pillar, and while running away dropped it on your toe."
			print "The toe got infected, and you died 7 months later..."
			print "Better luck next time!"
			break

def top_middle():
	print "You are at the top middle!\n"
	print "You can go east, south and west\n"
	print "\n"
	print "But wait... You find an open door!\n"
	print "You can choose to go through the door (type 'door')... or"
	print "you can choose to continue adventuring..."

	while True:
		direction = raw_input("> ")
		if direction == 'w':
			top_west()
			break
		if direction == 's':
			middle()
			break
		if direction == 'e':
			top_east()
			break
		if direction == 'door':
			door()
			break

def bottom_east():
	print "You are at the bottom east corner of the map!\n"
	print "You can go west and north!\n"

	while True:
		direction = raw_input("> ")
		if direction == 'w':
			bottom_middle()
			break
		elif direction == 'n':
			mid_east()
			break

def mid_east():
	print "You are at the middle of the east wall!\n"
	print "You can go north, south and west!\n"

	while True:
		direction = raw_input("> ")
		if direction == 'n':
			top_east()
			break
		elif direction == 's':
			bottom_east()
			break
		elif direction == 'w':
			middle()
			break

def top_east():
	print "You are at the top east!\n"
	print "You can go west and south!\n"

	while True:
		direction = raw_input("> ")
		if direction == 'w':
			top_middle()
			break
		elif direction == 's':
			mid_east()
			break

def door():
	print "You slowly creep through the door..."
	print "You stumble around, and manage to find a light switch."
	print "Do you turn in on? y/n."

	while True:
		direction = raw_input("> ")
		if direction == 'y':
			print "\n"
			print "You turned on the light, only to startle a mother grue!"
			print "In her attempts to save her young, she eats you."
			print "You were eaten by a Grue..."
			break
		if direction == 'n':
			print "\n"
			print "Wise choice..."
			print "After deciding to not switch on the light, you stumble around some more."
			print "To your amazement, you stepped on a teleporter which brought you home."
			print "You wake up in your bed and wonder if this was just a dream... Who knows?"
			print "GAME COMPLETED!"
			break

start()