import character

class Enemy(character.Character):
	def __init__(self):
		character.Character.__init__(self, "Enemy", 1, 3)
