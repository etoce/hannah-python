cases = {
	"is_sorted": [
		(([],), True),
		(([1],), True),
		(([1, 2, 3],), True),
		(([3, 2, 1],), False),
		(([1, 1, 1],), True),
		(([9, -1, 4, -1, 3, -3],), False),
		(([-100, 0, 0, 0, 0, 0, 0, 0, 0, 100],), True),
		(([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4],), False),
		(([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],), True)
	],
	"largest_number": [
		(([8],), 8),
		(([-3],), -3),
		(([1, 9, 3, 2, 10, 45, 4, 2, 1, 1, 1],), 45),
		(([-10, -2, -1, -8],), -1),
		(([11111, 22222, 33333, 44444],), 44444),
		(([100, 88, 2, -100, -88, 2],), 100)
	],
	"slice_and_glue": [
		(("",), ""),
		(("apple",), "pleap"),
		(("banana",), "anaban"),
		(("grapefruit",), "fruitgrape")
	],
	"double_characters": [
		(("",), ""),
		(("apple",), "aappppllee"),
		(("zzxxzz",), "zzzzxxxxzzzz")
	],
	"erer": [
		(("",), "er"),
		(("cat",), "cater"),
		(("care",), "carer"),
		(("unilever",), "unilever"),
		(("hannah",), "hannaher")
	],
	"is_anagram": [
		(("", ""), True),
		(("apple", "papel"), True),
		(("papel", "apple"), True),
		(("apple", "peal"), False),
		(("peal", "apple"), False),
		(("banana", "nab"), False),
		(("banana", "aaabnn"), True),
		(("apple", "lapel"), False),
	]
}