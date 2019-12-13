def countApplesAndOranges(s, t, a, b, apples, oranges):

	# calculate apples throws

	bad_oranges = 0

	throws_a = throwFruits(apples, a)
	throws_o = throwFruits(oranges, b)


	print(intersection(throws_a, s, t))
	print(intersection(throws_o, s, t))


def intersection(throws,s , t):

	bad_fruits = 0
	
	for i in range(len(throws)):

		if throws[i] >= s and throws[i] <= t:
			bad_fruits += 1
	
	return bad_fruits


def throwFruits(fruits, tree):
	final_pos = []
	for i in range(len(fruits)):
		final_pos.append(tree + fruits[i])

	return final_pos


apples = [2,3,-4] 
oranges = [3,-2,-4]


countApplesAndOranges(7, 10, 4, 12, apples, oranges)



