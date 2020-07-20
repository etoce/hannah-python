#
# one_dimensional_wordhunt()
#	Determines whether a word can be found in a one-dimensional Word Hunt grid.
# Parameters:
#	grid: A list representing a 1xN (where N is a positive integer) grid of characters
#	word: A string representing a possible word
# Return value:
#	True, if word can be found in grid, or false otherwise
# Implementation notes:
#	-
def substring_at_index(str1, str2, index):
	for i in range(len(str2)):
		if index + i >= len(str1) or str1[index + i] != str2[i]:
			return False
	return True

def substring_at_index_reverse(str1, str2, index):
	for i in range(len(str2)):
		if index - i < 0 or str1[index - i] != str2[i]:
			return False
	return True

def one_dimensional_wordhunt(grid, word):
	if word == "":
		return True
	for i in range(len(grid)):
		if substring_at_index(grid, word, i):
			return True
		if substring_at_index_reverse(grid, word, i):
			return True
	return False

#
# one_dimensional_wordhunt_with_wrap()
#	Determines whether a word can be found in a one-dimensional Word Hunt grid.
#	Wrapping is allowed (i.e. a word can start on one side of the grid and end
# 	on another, like how in the grid "altitude", "deal" is a valid word, as is
# 	"lae").
# Parameters:
#	grid: A list representing a 1xN (where N is a positive integer) grid of characters
#	word: A string representing a possible word
# Return value:
#	True, if word can be found in grid, or false otherwise
# Implementation notes:
#	-
def one_dimensional_wordhunt_with_wrap(grid, word):
	pass