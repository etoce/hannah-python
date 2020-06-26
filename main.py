import stringproblems
import stringanswers

moduleToTest = stringproblems

print(moduleToTest.contains("apple", "p"))
print(moduleToTest.contains("apple", "x"))
print(moduleToTest.contains("apple", "A"))

print(moduleToTest.isPalindrome("aardvark"))
print(moduleToTest.isPalindrome("racecar"))

print(moduleToTest.zipper("apple", "grapefruit"))
print(moduleToTest.zipper("grapefruit", "apple"))

moduleToTest.fizzBuzz(50)

print(moduleToTest.reverseString("Hello world!"))