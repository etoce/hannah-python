import stringproblems
import stringproblems2
import stringproblems2test
import stringproblems3
import stringproblems4
import stringproblems3test
import stringproblems4test
import stringanswers
import stringanswers2
import stringanswers3
import stringanswers4
import listproblems
import listanswers
import listproblemstest
import sortingproblems
import sortingproblemstest
import sortinganswers
import yahtzeeanswers
import yahtzeeproblems
import yahtzeetest
import tester

moduleToTest = yahtzeeanswers
testModule = yahtzeetest

myTester = tester.Tester(moduleToTest, getattr(testModule, "cases"))

myTester.testMethod("sum_of_dice")
myTester.testMethod("three_of_a_kind")
myTester.testMethod("full_house")
