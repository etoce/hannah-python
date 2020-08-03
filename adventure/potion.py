import item
import math

class Potion:
	def __init__(self, amount_healed):
		self.amount_healed = amount_healed

	def __str__(self):
		return str(self.amount_healed) + "hp potion"

	def use(self, user):
		user.hp = min(user.hp + self.amount_healed, user.maxhp)
		return True