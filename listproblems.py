#
# is_sorted()
# 	Determines whether a given list of numbers is sorted from smallest to
#	largest. A list is sorted if there is no pair of elements where the
#	element that appears later in the list is smaller than the element that 
# 	appears earlier in the list.
# Parameters:
#	list: A list of numbers, comparable with the >, >=, <, and <= operators.
# Return value:
#	True, if the list is sorted, or false otherwise.
# Implementation notes:
#	Do not use Python's built-in List.sort() method.
def is_sorted(list):
	return "To be implemented"

#
# largest_number()
# 	Given a list of numbers, finds and returns the largest number in the list.
# Parameters:
#	list: A non-empty list of numbers
# Return value:
#	The value of the largest number in the list
# Implementation notes:
#	Do not use Python's built-in max() function.
def largest_number(list):
	return "To be implemented"

#
# slice_and_glue()
# 	Given a string, cut it in half and glue together the two halves in
#	reverse order. "Half" is defined as dividing the string into parts such
#	that the two halves are as equal in length as possible, with the first
#	half getting the extra character if the string has an odd number of
#	characters. For example, slice_and_glue("apple") should return "leapp".
# Parameters:
#	str: The string in question
# Return value:
#	A mangled version of a string that has undergone disfiguring surgery for
#	the sake of an education.
# Implementation notes:
#	Python has a special way to slice strings using the syntax str[start:end].
#	For example, "apple"[1:4] has the value "ppl".
def slice_and_glue(str):
	return "To be implemented"

#
# double_characters()
# 	Given a string, return a string with each of the original string's 
# 	characters doubled. For example, if str is "apple", this function should
#	return "aappppllee".
# Parameters:
#	str: The string in question
# Return value:
#	A string with each of the characters of str doubled.
# Implementation notes:
#	-
def double_characters(str):
	return "To be implemented"

#
# erer()
#	Adds "-er" to a string. If the string already ends in -er, add nothing. If
#	the string ends in "-e", only add an "r".
# Parameters:
#	str: The string in question
# Return value:
#	The er-ified string
# Implementation notes:
#	-
def erer(str):
	return "To be implemented"

#
# is_anagram()
#	Determines if two strings are anagrams of each other. Two strings are
#	anagrams if they both contain the same characters in the same quantities.
# 	For example, "papel" is an anagram of "apple", while "lapel" is not. Note 
# 	that every string is an anagram of itself according to this definition.
# Parameters:
#	str1: The first string in question
#	str2: The second string in question
# Return value:
#	True, if str1 and str2 are anagrams, or false, if they are not.
# Implementation notes:
#	-
def is_anagram(str1, str2):
	return "To be implemented"