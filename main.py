import stringproblems
import stringproblems2
import stringproblems2test
import stringanswers
import stringanswers2
import listproblems
import listanswers
import listproblemstest
import tester

moduleToTest = listproblems
testModule = listproblemstest

myTester = tester.Tester(moduleToTest, getattr(testModule, "cases"))

#myTester.testMethod("is_sorted")
#myTester.testMethod("largest_number")
#myTester.testMethod("slice_and_glue")
#myTester.testMethod("double_characters")
#myTester.testMethod("erer")
#myTester.testMethod("is_anagram")

