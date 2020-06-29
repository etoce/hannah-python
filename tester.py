class Tester:
	def __init__(self, moduleToTest, cases):
		self.moduleToTest = moduleToTest
		self.cases = cases
	
	def testMethod(self, methodName):
		if methodName in self.cases:
			testsRun = 0
			successes = 0
			failures = 0
			for testCase in self.cases[methodName]:
				if hasattr(self.moduleToTest, methodName):
					print("Testing " + methodName + "" + str(testCase[0]))
					testsRun += 1
					returnValue = getattr(self.moduleToTest, methodName)(*testCase[0])
					if returnValue != testCase[1]:
						failures += 1
						if isinstance(testCase[1], str):
							print("Test failed: got " + str(returnValue) + ", but expected \"" + str(testCase[1]) + "\"")
						else:
							print("Test failed: got " + str(returnValue) + ", but expected " + str(testCase[1]))
					else:
						successes += 1
						print("Test passed! Return value of " + str(returnValue) + " matches expected value!")
		print("Finished testing " + methodName + "(); " + str(testsRun) + " tests, " + str(successes) + " pass(es), " + str(failures) + " failures")

