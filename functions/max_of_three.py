def max_of_three(a, b, c):	
	if a >= b and a >= c:
		return a
	elif b >= a and b >= c:
		return b
	elif c >= b and c >= a:
		return c
while True:
	numbers = input("Enter Three Numbers: ")	# a, b, c = map(int, numbers.split(" "))
	if numbers == "quit":
		break 
	a, b, c = map(int, numbers.split(" "))
	print(max_of_three(a, b, c))
