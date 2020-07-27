import sys

# Lyrics to the song "Do-Re-Mi" from "The Sound of Music"
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

# You can also modify values in a dictionary like you can in a list:

example["do"] = "A deer, an email deer"
print(example["do"])
example["do"] = "A deer, an female deer" # Change it back to be nice

# You can also use that syntax to add entries to the dictionary if they don't
# exist:

example["not_a_note"] = "haha"
print(example)
example.pop("not_a_note")	# Remove the entry; no littering!

# You can loop through dictionaries using the same syntax as lists. However,
# while doing this with lists gives you the elements (i.e. the values), 
# looping through dictionaries like this gives you the keys (analogous to a 
# list's indices).

for x in example:
	print(x)	# Prints "do", "re", "mi", etc., but not necessarily in order

# You can also loop through the dictionary's keys explicitly like this:

for x in example.keys():
	print(x)	# Prints "do", "re", "mi", etc., but not necessarily in order

# If you want the dictionary's values, you can use the [] syntax described 
# above.

for x in example:
	print(example[x])	# Prints "A deer, a female deer", "A drop of golden sun", etc.

# You can also loop through the values explicitly, just like with the keys:

for x in example.values():
	print(x)			# Prints "A deer, a female deer", "A drop of golden sun", etc.

# Alternatively, you can use items() to loop through a dictionary and have both
# the keys and the values as iterating variables.

for x, y in example.items(): # x is the key and y is the value
	print("key: " + str(x))
	print("value: " + str(y))

# Okay, now you know a zillion things about dictionaries.

# This is a dictionary representing the twelve months of the Gregorian 
# calendar and the number of days they have in non-leap years
months = {
	"january": 31,
	"february": 28,
	"march": 31,
	"april": 30,
	"may": 31,
	"june": 30,
	"july": 31,
	"august": 31,
	"september": 30,
	"october": 31,
	"november": 30,
	"december": 31
}

# Print the number of days in April:



# Print all the months that have 31 days:



# Print the total number of days in the year:




# A dictionary representing playable characters in the video game Persona 4.
# Persona 4 is a role-playing video game developed and published by Atlus. It 
# is chronologically the fifth installment in the Persona series, itself a part
# of the larger Megami Tensei franchise, and was released for the PlayStation 2
# in Japan in July 2008, North America in December 2008, and Europe in March 
# 2009. It was re-released as a PlayStation 2 Classic for the PlayStation 3 in 
# April 2014. Persona 4 takes place in a fictional Japanese countryside and is 
# indirectly related to earlier Persona games. The player-named protagonist is 
# a high-school student who moved into the countryside from the city for a 
# year. During his year-long stay, he becomes involved in investigating 
# mysterious murders while harnessing the power of summoning Persona. The game 
# features a weather forecast system with events happening on foggy days to 
# replace the moon phase system implemented in the previous games.
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



# Print "odd" if there is an odd number of male characters, or "even" if there
# is an even number of male characters:



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