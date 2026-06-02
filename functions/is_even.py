def is_even(number):
	if int(number) % 2 == 0:
		return True
	else:
		return False
while True: 
	number = input("Is your number even?: ")
	if number == "quit":
		break
	print(is_even(number))
