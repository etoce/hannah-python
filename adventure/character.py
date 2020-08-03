class Character:
	# The __init__ function defines what happens when an object of this class 
	# is created.
	def __init__(self, name, level, maxhp):
		self.name = name
		self.level = level
		self.maxhp = maxhp
		self.hp = maxhp

	# Functions inside the class body take "self" as the first parameter, which
	# represents the object that it is called on.
	def print_status(self):
		print(self.name)
		print("Level: " + str(self.level))
		print("HP: " + str(self.hp) + "/" + str(self.maxhp))
	
	def attack(self, other):
		print(self.name + " attacks " + other.name + "!")
		damage = min(self.level - other.level + 2, 1)
		print(self.name + "'s attack deals " + str(damage) + " damage!")
		other.hp = other.hp - damage
		print(other.name + " is now at " + str(other.hp) + "/" + str(other.maxhp) + "hp")

	def is_dead(self):
		return self.hp <= 0

	def level_up(self):
		self.level = self.level + 1
		self.maxhp = self.maxhp + 5