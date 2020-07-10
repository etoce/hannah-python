import stringproblems
import stringproblems2
import stringproblems2test
import stringproblems3
import stringproblems3test
import stringanswers
import stringanswers2
import stringanswers3
import listproblems
import listanswers
import listproblemstest
import sortingproblems
import sortingproblemstest
import sortinganswers
import tester

moduleToTest = stringanswers3
testModule = stringproblems3test

myTester = tester.Tester(moduleToTest, getattr(testModule, "cases"))

#myTester.testMethod("substring")
myTester.testMethod("contains_letters")
