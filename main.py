import stringproblems
import stringproblems2
import stringproblems2test
import stringanswers
import stringanswers2
import tester

moduleToTest = stringproblems2
testModule = stringproblems2test

myTester = tester.Tester(moduleToTest, getattr(testModule, "cases"))

#myTester.testMethod("parrot")
#myTester.testMethod("scrabbleScore")
#myTester.testMethod("hasDuplicateLetters")
#myTester.testMethod("collatzSteps")

