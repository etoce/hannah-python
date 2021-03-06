from copy import deepcopy

class Tester:
	def __init__(self, moduleToTest, cases):
		self.moduleToTest = moduleToTest
		self.cases = cases
	
	def format(self, thing):
		if isinstance(thing, str):
			return "\"" + thing + "\""
		else:
			return str(thing)

	def formatTupleAsArguments(self, tuple):
		strTuple = str(tuple).replace("'", "\"")
		if len(tuple) == 1:
			return strTuple[0:len(strTuple) - 2] + strTuple[len(strTuple) - 1]
		else:
			return strTuple
	
	def testMethod(self, methodName):
		if methodName in self.cases:
			runs = 0
			successes = 0
			failures = 0
			for testCase in self.cases[methodName]:
				if hasattr(self.moduleToTest, methodName):
					input = deepcopy(testCase[0])
					runs += 1
					returnValue = getattr(self.moduleToTest, methodName)(*input)
					if returnValue != testCase[1]:
						failures += 1
						print("Test failed: " + methodName + self.formatTupleAsArguments(testCase[0]) + " returned " + self.format(returnValue) + " instead of the expected " + self.format(testCase[1]))
					else:
						successes += 1
						print("Test passed! " + methodName + self.formatTupleAsArguments(testCase[0]) + " returned " + self.format(returnValue) + ", matching the expected value!")
			message = ""
			if successes == runs:
				message = "Perfect!"
			elif successes / runs >= 0.75:
				message = "Getting close!"
			elif successes / runs >= 0.5:
				message = "I guess it could be worse."
			elif successes / runs > 0:
				message = "Hey, at least they didn't all fail, right?"
			else:
				message = "Aw, it's okay. Just think of all the progress you're about to make!"
			print("Finished testing " + methodName + "(): " + str(successes) + " of " + str(runs) + " tests passed.")
			print(message)

