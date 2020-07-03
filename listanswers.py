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
	for i in range(1, len(list)):
		if (list[i] < list[i-1]):
			return False
	return True


#
# largest_number()
# 	Given a list of numbers, finds and returns the largest number in the list.
# Parameters:
#	list: A list of numbers
# Return value:
#	The value of the largest number in the list
# Implementation notes:
#	Do not use Python's built-in max() function.
def largest_number(list):
	candidate = list[0]
	for number in list:
		if number > candidate:
			candidate = number
	return candidate

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
	return str[len(str) // 2 : len(str)] + str[0 : len(str) // 2]

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
	doubled = ""
	for char in str:
		doubled = doubled + char + char
	return doubled

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
	if len(str) > 0 and str[len(str)-1] == "e":
		return str + "r"
	elif len(str) > 1 and str[len(str)-2:len(str)] == "er":
		return str
	else:
		return str + "er"

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
	if len(str1) != len(str2):
		return False
	indices_accounted_for = set()
	for char1 in str1:
		for i in range(len(str2)):
			if char1 == str2[i] and not i in indices_accounted_for:
				indices_accounted_for.add(i)
				break
			if i == len(str2) - 1:
				return False
	return True


