class ComparisonBox:
	def __init__(self):
		self.calls = 0
	
	def compare(self, a, b):
		self.calls += 1
		if a < b:
			return 1
		elif b > a:
			return -1
		else:
			return 0