#
# parrot()
#	Creates a string that is the given string, repeated n times. For example,
#	if str is "apple" and n is 3, this function should return "appleappleapple".
# Parameters:
#	str: The string to repeat
#	n: The number of times to repeat
# Return value:
#	A single string consisting of str, repeated n times. If n is 0, return an
#	empty string (""). 
# Implementation notes:
#	You may assume that n is a positive integer and that it is not so big that
#	it crashes your computer.
def parrot(str, n):
	retValue = ""
	for i in range(n):
		retValue += str
	return retValue

#
# scrabbleScore()
#	Calculates the score that the given word would receive in the word game
#	Scrabble (c), disregarding board effects such as Double Word Scores.
#	If the string contains characters that are not valid Scrabble (c) tiles,
#	ignore them.
# Parameters:
#	str: The word in question
# Return value:
#	True, if str1 contains all the letters of str2, or false, if it does not.
# Implementation notes:
#	Use this table when determining letter scores:
#	Letter							Score
#	A, E, I, L, N, O, R, S, T, U	1
#	D, G							2
#	B, C, M, P						3
#	H, F, V, W, Y					4
#	K								5
#	J, X							8
#	Q, Z							10
def scrabbleScore(str):
	strLower = str.lower()
	score = 0
	for char in strLower:
		if char == "a" or char == "e" or char == "i" or char == "l" or char == "n" or char == "o" or char == "r" or char == "s" or char == "t" or char == "u":
			score += 1
		elif char == "d" or char == "g":
			score += 2
		elif char == "b" or char == "c" or char == "m" or char == "p":
			score += 3
		elif char == "h" or char == "f" or char == "v" or char == "w" or char == "y":
			score += 4
		elif char == "k":
			score += 5
		elif char == "j" or char == "x":
			score += 8
		elif char == "q" or char == "z":
			score += 10
	return score

#
# hasDuplicateLetters()
#	Determines if a given string has at least two of the same character.
# Parameters:
#	str: The string in question
# Return value:
#	True, if the string contains a duplicate character, or false otherwise.
# Implementation notes:
#	Consider upper- and lower-case characters distinct for the purposes of 
#	this exercise.
def hasDuplicateLetters(str):
	for i in range(len(str)):
		for j in range(len(str)):
			if i != j and str[i] == str[j]:
				return True
	return False

#
# collatzSteps()
#	Determines how many steps are needed to reach 1 in the sequence described
#	by the Collatz conjecture (also known as the Hail Problem). The procedure
#	is thus:
#
#	Begin with a positive integer n. If it is odd, multiple it by 3 and add 1.
#	If it is even, divide it by 2. Repeat this process with the result until
#	either the result is 1 or you repeat a number already encountered.
#
#	As an example, try starting with the number 7:
#		7 -> odd, so 7 * 3 + 1 = 22
#		22 -> even, so 22 / 2 = 11
#		11 -> odd, so 11 * 3 + 1 = 34
#		34 -> even, so 34 / 2 = 17
#		17 -> odd, so 17 * 3 + 1 = 52
#		52 -> even, so 52 / 2 = 26
#		26 -> even, so 26 / 2 = 13
#		13 -> odd, so 13 * 3 + 1 = 40
#		40 -> even, so 40 / 2 = 20
#		20 -> even, so 20 / 2 = 10
#		10 -> even, 10 / 2 = 5
#		5 -> odd, so 5 * 3 + 1 = 16
#		16 -> even, so 16 / 2 = 8
#		8 -> even, so 8 / 2 = 4
#		4 -> even, so 4 / 2 = 2
#		2 -> even, so 2 / 2 = 1
#		1 is 1, so we are done with 16 steps
# Parameters:
#	n: The starting number, a positive integer
# Return value:
#	The number of steps required to reach 1, or -1 if it never does.
# Implementation notes:
#	People have tried very hard to find a positive integer that never reaches 1
#	and have failed.
def collatzSteps(n):
	steps = 0
	num = n
	while num != 1:
		steps += 1
		if num % 2 == 0:
			num = num / 2
		else:
			num = (num * 3) + 1
		if steps > 100:
			break
	return steps