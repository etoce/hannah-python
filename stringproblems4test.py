cases = {
	"one_dimensional_wordhunt": [
		(("", ""), True),
		(("a", "a"), True),
		(("apple", ""), True),
		(("", "apple"), False),
		(("apple", "app"), True),
		(("apple", "ppa"), True),
		(("apple", "ppl"), True),
		(("apple", "ape"), False),
		(("apple", "peal"), False),
		(("apple", "apl"), False),
		(("apple", "elp"), True),
		(("apple", "pa"), True),
		(("apple", "pael"), False),
		(("apple", "leap"), False)
	],
	"one_dimensional_wordhunt_with_wrap": [
		(("", ""), True),
		(("a", "a"), True),
		(("apple", ""), True),
		(("", "apple"), False),
		(("apple", "app"), True),
		(("apple", "ppa"), True),
		(("apple", "leap"), True),
		(("apple", "pael"), True),
		(("apple", "aep"), False),
		(("apple", "leppa"), False),
		(("apple", "lpa"), False)
	]
}