import player
import character
import potion
import enemy

p = player.Player()
p.add_item(potion.Potion(10))

def start():
	print("Welcome to Adventure Town, where adventurers come to fulfill their destiny!")
	print("Type \"help\" to get started or \"quit\" to leave.")
	while True:
		print(">", end=" ")
		line = input()
		if line == "quit":
			quit()
		else:
			handle_input(line)

def quit():
	print("Bye!", end=" ")
	exit(0)

def handle_input(line):
	parts = line.split()
	if parts[0] == "help":
		print("Available commands:")
		print("  status: Displays your current status")
		print("  inventory: Displays the items in your inventory")
		print("  use-item <item_number>: Uses an item")
	elif parts[0] == "status":
		p.print_status()
	elif parts[0] == "inventory":
		print("Inventory:")
		for i in range(len(p.inventory)):
			print(str(i) + ". " + str(p.inventory[i]))
	elif parts[0] == "use-item":
		if len(parts) > 0:
			try:
				index = int(parts[1])
				item = p.inventory[index]
				p.use_item(index)
				print(str(item) + " used.")
			except ValueError:
				print("Argument must be a positive integer.")
			except IndexError:
				print("Given item index is invalid. Please try again.")
		else:
			print("Tell me what item to use!")
	elif parts[0] == "explore":
		print("An enemy appears!")
		p.set_battle_opponent(enemy.Enemy())
		p.battle_opponent.print_status()
		while True:
			print("What will you do?")
			print("0. Fight")
			print("1. Run")
			l = input()
			try:
				if l == "0":
					p.attack(p.battle_opponent)
					if p.battle_opponent.is_dead():
						print("You win!")
						p.level_up()
						print("Level up! You are now level " + str(p.level))
						p.set_battle_opponent(None)
						break
					p.battle_opponent.attack(p)
				elif l == "1":
					print("You run away.")
					p.set_battle_opponent(None)
					break
				elif l == "quit":
					quit()
				else:
					print("Please type something reasonable.")
			except ValueError:
				print("Please type something reasonable.")
			
	else:
		print("Bzzt! Invalid command! Maybe try \"help\"?")

start()
