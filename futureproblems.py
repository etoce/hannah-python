#
# substring()
# 	Determines whether a given string contains another string. In order for a
#   string to contain another, it must have all the characters in the second
# 	string in the exact same order. For example, the string "apple" contains 
#	"ap", but does not contain "ape". And to clarify, the empty string ("") is
#	considered a substring of every string.
# Parameters:
#	str: The string to search through
#	potentialSubstring: The string to look for
# Return value:
#	True, if str contains potentialSubstring, or false, if it does not.
# Implementation notes:
#	Do not use any external libraries that may implement this functionality.
def substring(str, potentialSubstring):
	return "To be implemented"

#
# indexOfSubstring()
# 	Determines the index of the first occurrence of a string in another. For
#	example, if str is "The quick brown apple jumped through the apple apple"
#	and potentialSubstring is "apple", this function should return 16.
# Parameters:
#	str: The string to search through
#	potentialSubstring: The string to look for
# Return value:
#	The index of the first occurrence of potentialSubstring in str, or -1 if
#	str does not contain potentialSubstring.
# Implementation notes:
#	Do not use any external libraries that may implement this functionality.
def indexOfSubstring(str, potentialSubstring):
	return "To be implemented"

#
# isAnagramOf()
#	Determines if two strings are anagrams of each other. Two strings are
#	anagrams if they both contain the same characters in the same quantities.
#  For example, "papel" is an anagram of "apple", while "lapel"
# 	is not. Note that every string is an anagram of itself according to this
#	definition.
# Parameters:
#	str1: The first string in question
#	str2: The second string in question
# Return value:
#	True, if str1 and str2 are anagrams, or false, if they are not.
# Implementation notes:
#	-
def isAnagramOf(str1, str2):
	return "To be implemented"

#
# containsLettersOf()
#	Determines if a given string contains the letters of another given string
#	within it, disregarding order. For example, the string "apple" contains the
#	letters in the string "peal", even though the string "peal" is not a
#	substring of "apple". Additionally, if str2 contains duplicates of a letter,
# 	it must appear twice (or more) in str1 in order for this function to return
#	true. For example, if str1 is "apple" and str2 is "peel", this function
#	should return false because even though "apple" has one "e", "peel" has two,
#	so "apple" does not contain the letters of "peel".
# Parameters:
#	str1: The string in which to search for the letters of str2
#	str2: The string whose letters we want to look for in str1
# Return value:
#	True, if str1 contains all the letters of str2, or false, if it does not.
# Implementation notes:
#	-
def containsLettersOf(str1, str2):
	return "To be implemented"