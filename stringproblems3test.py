cases = {
	"substring": [
		(("", ""), True),
		(("a", "a"), True),
		(("apple", ""), True),
		(("", "apple"), False),
		(("apple", "app"), True),
		(("apple", "ple"), True),
		(("apple", "ppl"), True),
		(("apple", "app"), True),
		(("apple", "ape"), False),
		(("apple", "peal"), False),
		(("apple", "apl"), False)
	],
	"contains_letters": [
		(("", ""), True),
		(("a", "a"), True),
		(("apple", ""), True),
		(("", "apple"), False),
		(("apple", "ppl"), True),
		(("apple", "peal"), True),
		(("apple", "leap"), True),
		(("apple", "lapel"), False),
		(("apple", "papel"), True),
		(("apple", "papal"), False)
	]
}