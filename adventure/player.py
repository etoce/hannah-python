import character

# If a class is a subclass of another class, it is indicated by a set of
# parentheses with the superclass inside.
class Player(character.Character):
	def __init__(self):
		character.Character.__init__(self, "Player", 1, 10)
		self.inventory = []
		self.battle_opponent = None
	
	def add_item(self, item):
		self.inventory.append(item)

	def use_item(self, index):
		if self.inventory[index].use(self):
			self.inventory.pop(index) # Remove if it says to remove

	def set_battle_opponent(self, opponent):
		self.battle_opponent = opponent

	