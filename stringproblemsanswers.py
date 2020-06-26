# Purpose:
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
# Reverses the characters of a string.
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

#
# Finds the index of the first occurence of a character in a string.
# Parameters:
#	str: The string to examine
#	char: The character to search for
# Return value:
#	The index of the first occurence of char in str, or -1 if char is not found
# 	in str. For example, if str has the value "apple", and char has the value 
# 	"p", the return value should be 1. If str has the value "apple" and char has
#	the value "x", the return value should be -1.
#

def indexOf(str, char):
	for i in range(len(str)):
		if char == str[i]:
			return i
	return -1





fizzBuzz(50)

