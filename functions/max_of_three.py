def max_of_three(a, b, c):
	if a >= b and a >= c:
		return a
	elif b >= a and b >= c:
		return b
	elif c >= b and c >= a:
		return c
print(max_of_three(123122, 432432, 12343))
