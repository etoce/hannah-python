cases = {
	"move_element_within_list": [
		(([3], 0, 0), [3]),
		(([1, 2, 3], 2, 0), [3, 1, 2]),
		(([1, 2, 3], 2, 2), [1, 2, 3]),
		(([4, 7, 10, 13, 16], 2, 4), [4, 7, 13, 16, 10]),
		(([10, 9, 8, 7, 6], 4, 0), [6, 10, 9, 8, 7])
	],
	"insertion_sort": [
		(([],), []),
		(([1],), [1]),
		(([1, 2, 3],), [1, 2, 3]),
		(([5, 1, 4, 7, 2, 6],), [1, 2, 4, 5, 6, 7]),
		(([9, 3, 6, 1, 3, 2, 2, 4],), [1, 2, 2, 3, 3, 4, 6, 9])
	],
	"merge_sorted_lists": [
		(([],[]), []),
		(([1],[]), [1]),
		(([],[1]), [1]),
		(([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
		(([1, 5, 10, 12, 15], [2, 3, 4]), [1, 2, 3, 4, 5, 10, 12, 15])
	],
	"merge_sort": [
		(([],), []),
		(([1],), [1]),
		(([1, 2, 3],), [1, 2, 3]),
		(([5, 1, 4, 7, 2, 6],), [1, 2, 4, 5, 6, 7]),
		(([9, 3, 6, 1, 3, 2, 2, 4],), [1, 2, 2, 3, 3, 4, 6, 9])
	]
}