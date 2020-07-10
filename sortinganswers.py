#
# move_element_within_list()
#	Moves an element from one part of a list to another part of the list. The
#	other elements of the list should be shifted to accommodate the new
#	position of the moved element such that the list contains the same elements
#	at the end as it did in the beginning, only in different positions.
# Parameters:
#	list: The list in question
#	old_index: The index of the element to be moved
#	new_index: The index where the element is to be moved to
# Return value:
# 	The list, with the element at list[old_index] moved to new_index.
# Implementation notes:
#	-
def move_element_within_list(list, old_index, new_index):
	if old_index == new_index:
		return list
	elif old_index > new_index:
		return list[0:new_index] + [list[old_index]] + list[new_index:old_index] + list[old_index+1:len(list)]
	else:
		return list[0:old_index] + list[old_index+1:new_index+1] + [list[old_index]] + list[new_index+1:len(list)]

#
# insertion_sort()
# 	Given a list, sorts it using the "insertion sort" algorithm.
# Parameters:
#	list: A list with elements comparable with the <, <=, >, >=, and == operators
# Return value:
#	A sorted version of the list.
# Implementation notes:
#	Do not use Python's built-in List.sort() or your own sorting functions.
def insertion_sort2(list):
	for i in range(len(list)):
		for j in range(i):
			if list[j] > list[i]:
				list = list[0:j] + [list[i]] + list[j:i] + list[i+1:len(list)]
				#list = move_element_within_list(list, i, j)
				break
	return list

def insertion_sort(list):
	for i in range(len(list)):
		num = list[i]
		j = i - 1
		while j >= 0 and list[j] > num:
			list[j + 1] = list[j]
			j -= 1
		list[j + 1] = num
	return list

#
# merge_sorted_lists()
# 	Given two lists that are already sorted, combine them into one list that
#	is also sorted.
# Parameters:
#	list1: A list of numbers sorted from smallest to largest
#	list2: A list of numbers sorted from smallest to largest
# Return value:
#	A list containing the elements of list1 and list2 that is also sorted from
#	smallest to largest
# Implementation notes:
#	Do not use Python's built-in List.sort() or your own sorting functions. You
#	can do this without doing a full sort of the finished list.
def merge_sorted_lists(list1, list2):
	i = 0
	j = 0
	merged = []
	while i < len(list1) or j < len(list2):
		if i >= len(list1):
			merged.append(list2[j])
			j += 1
		elif j >= len(list2):
			merged.append(list1[i])
			i += 1
		else:
			if list1[i] > list2[j]:
				merged.append(list2[j])
				j += 1
			else:
				merged.append(list1[i])
				i += 1
	return merged

#
# merge_sort()
# 	Given a list, sort it using the "mergesort" algorithm.
# Parameters:
#	list: A list with elements comparable with the <, <=, >, >=, and == operators
# Return value:
#	A sorted version of the list.
# Implementation notes:
#	Do not use Python's built-in List.sort() or your own sorting functions.
#	You are encouraged to use the merge_sorted_lists() that you implemented 
#	earlier in this module.
def merge_sort(list):
	if len(list) <= 1:
		return list
	left_half = list[0:len(list)//2]
	right_half = list[len(list)//2:len(list)]
	return merge_sorted_lists(merge_sort(left_half), merge_sort(right_half))