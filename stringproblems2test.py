cases = {
	"parrot": [
		(("", 3), ""),
		(("apple", 3), "appleappleapple"),
		(("zzzzzzz", 10), "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
	],
	"withoutVowels": [
		(("",), ""),
		(("cry",), "cry"),
		(("apple",), "ppl"),
		(("crystal",), "crystl"),
		(("facetiously",), "fctsly"),
		(("oea",), "")
	],
	"scrabbleScore": [
		(("",), 0),
		(("apple",), 9),
		(("quick",), 20),
		(("brown",), 10),
		(("fox",), 13),
		(("jumped",), 18),
		(("over",), 7),
		(("the",), 6),
		(("lazy",), 16),
		(("dog",), 5),
	],
	"hasDuplicateLetters": [
		(("",), False),
		(("apple",), True),
		(("label",), True),
		(("facetiously",), False),
		(("country",), False),
		(("apogee",), True)
	],
	"collatzSteps": [
		((1,), 0),
		((8,), 3),
		((7,), 16),
		((91,), 92)
	]
}