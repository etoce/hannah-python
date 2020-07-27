import sys

example = {
	"do": "A deer, a female deer",
	"re": "A drop of golden sun",
	"mi": "A name I call myself",
	"fa": "A long long way to run",
	"so": "A needle pulling thread",
	"la": "A note to follow so",
	"ti": "A drink with jam and bread"
}

# Think of a dictionary as a list where, instead of the elements being in
# order, they're floating around in space and the only way to retrieve them is
# by using the key that they're attached to.
#
# With a list, you access the elements by using [] and the index of the
# element you want. Dictionaries are similar, except instead of an index, we 
# use a key.

print(example["do"])	# Prints "A deer, a female deer"

# Like lists, dictionaries can be used with the len() function.

print(len(example)) 	# Prints 7

# You can loop through dictionaries using the same syntax as with lists. 
# However, even though doing this with lists gives you the elements (i.e. 
# the values), looping through dictionaries like this gives you the keys
# (analogous to a list's indices).

for x in example:
	print(x)	# Prints "do", followed by "re", following by "mi", etc.

# If you want the dictionary's values, you can use the [] syntax described 
# above.

for x in example:
	print(example[x])	# Prints "A deer, a female deer", "A drop of golden sun", etc.

# Alternatively, you can use items() to loop through a dictionary and have both
# the keys and the values as iterating variables.

for x, y in example.items(): # x is the key and y is the value
	print("key: " + str(x))
	print("value: " + str(y))


persona_4_characters = {
	"Yu": {
		"last_name": "Narukami",
		"year": 2,
		"arcana": "Fool",
		"gender": False
	},
	"Yosuke": {
		"last_name": "Hanamura",
		"year": 2,
		"arcana": "Magician",
		"gender": False
	},
	"Chie": {
		"last_name": "Satonaka",
		"year": 2,
		"arcana": "Chariot",
		"gender": True
	},
	"Yukiko": {
		"last_name": "Amagi",
		"year": 2,
		"arcana": "Priestess",
		"gender": True
	},
	"Kanji": {
		"last_name": "Tatsumi",
		"year": 1,
		"arcana": "Emperor",
		"gender": False
	},
	"Rise": {
		"last_name": "Kujikawa",
		"year": 1,
		"arcana": "Lovers",
		"gender": True
	},
	"Naoto": {
		"last_name": "Shirogane",
		"year": 1,
		"arcana": "Fortune",
		"gender": True
	}
}

# Print Chie's full name, her year, and her Major Arcana:



# Print the full names of every Persona 4 character in the dictionary:



# Print the full names of every female (gender: True) Persona 4 character in 
# the dictionary:



# Print all the Major Arcana represented by a first-year student:



# Print "True" if there is an odd number of male characters, or "False" if
# there is an even number of male characters:



# Create a list of all the first names in the dictionary, then print the list:




#
# longest_definition()
#	Given a dictionary (str -> str), finds the key that corresponds to the
#	longest value. If the dictionary is empty, return an empty string.
# Parameters:
#	dict: The dictionary
# Return value:
#	The key value with the longest definition. For example, with the do-re-mi 
# 	example, longest_definition(example_dictionary) should return "ti".
# Implementation notes:
#	-

def longest_definition(dict):
	pass

#print(longest_definition(example)) # Running this line of code should print "ti".


#
# flip_dictionary()
#	Given a dictionary (str -> str), creates and returns a new dictionary
#	where the first dictionary's values are the keys and the first fictionary's
#	keys are the values. For example, if done on the example dictionary above,
#	the new dictionary should have entries like this:
#
# 	"A deer, a female deer": "do"
#	"A drop of golden sun": "re"
#	etc.
#
# Parameters:
#	dict: The first dictionary
# Return value:
#	A dictionary where each entry corresponds to an entry in dict, but with the
#	key and value reversed.
# Implementation notes:
#	-
def flip_dictionary(dict):
	pass