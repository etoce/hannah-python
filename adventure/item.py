class Item:
	def __init__(self):
		pass
	
	# Returns True if the item should be removed from the inventory after use,
	# or False otherwise.
	def use_item(self, user):
		return True