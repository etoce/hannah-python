#
# contains()
# 	Determines if a string contains a given character
# Parameters:
#	str: The string to examine
#	char: The character to search for
# Return value:
#	True, if the string contains the character, or false, if it does not. Note
#	that we care about the exact character, so "A" is not the same as "a".
# Implementation notes:
#	-
#
def contains(str, char):
	for c in str:
		if c == char:
			return True
	return False

#
# indexOf()
# 	Finds the index of the first occurence of a character in a string.
# Parameters:
#	str: The string to examine
#	char: The character to search for
# Return value:
#	The index of the first occurence of char in str, or -1 if char is not found
# 	in str. For example, if str has the value "apple", and char has the value 
# 	"p", the return value should be 1. If str has the value "apple" and char has
#	the value "x", the return value should be -1.
# Implementation notes:
#	When looping through the characters of the string, you can use either 
# 	enumerate() or range() to gain access to the index. Remember that you can
#	use len() to determine the length of a string if you need to.
#
def indexOf(str, char):
	for i in range(len(str)):
		if char == i:
			return i
	return -1

#
# isPalindrome()
# 	Determines whether a given string is a palindrome (i.e. reads the same
# 	back-to-front as front-to-back)
# Parameters:
#	str: The string in question
# Return value:
#	True, if the string is a palindrome, or false, if it is not. The empty
# 	string ("") is a palindrome.
# Implementation notes:
#	-
#
def isPalindrome(str):
	for i in range(len(str) // 2):
		if str[i] != str[len(str) - i - 1]:
			return False
	return True

#
# zipper()
# 	Takes two strings and merges them together one character at a time with
# 	str1 existing in the even indices and str2 existing in the odd indices.
#	If one string is longer than the other, the remaining parts of that string
#	should be appended to the end. For example, if str1 is "apple" and str2 is
#   "grapefruit", this function should return "agprpalpeefruit".
# Parameters:
#	str1: The first string in question
#	str2: The second string in question
# Return value:
#	The merged value of the two strings.
# Implementation notes:
#	-
def zipper(str1, str2):
	returnString = ""
	for i in range(max(len(str1), len(str2))):
		if i < len(str1):
			returnString = returnString + str1[i]
		if i < len(str2):
			returnString = returnString + str2[i]
	return returnString

#
# fizzBuzz()
# 	Prints the integers from 1 to n with the following exceptions:
#		- If the integer is a multiple of 3, print "Fizz" instead.
#		- If the integer is a multiple of 5, print "Buzz" instead.
#		- If the integer is a multiple of both 3 and 5, print "FizzBuzz" instead.
# Parameters:
#	str: The string to reverse
# Return value:
#	A string with the characters of str in reverse order
#
def fizzBuzz(n):
	for i in range(n):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

#
# reverseString()
# 	Reverses the characters of a string.
# Parameters:
#	str: The string to reverse
# Return value:
#	A string with the characters of str in reverse order
#
def reverseString(str):
	reversed = ""
	for c in str:
		reversed = c + reversed
	return reversed

