def kangaroo(x1, v1, x2, v2):


	big = abs(x1-x2)
	a = v1 * big
	b = v2 * big
	
	print(a/b % v2)

	
# kangaroo(0, 2, 5, 3)


kangaroo(2081, 8403, 9107, 8400)

