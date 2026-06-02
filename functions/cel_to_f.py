# c = input("what's the tempurature int celcius? ")
def c_to_f(c): return (c * 1.8 + 32)
while True:
	c = input("what's the temp in celcius? ")
	if c == ("quit"):
		break
	else:
		print(c_to_f(int(c)))
		# c = input("what's the temp in celcius? ")
	# print(c_to_f(int(c)))
	# if c == ("quit"):
		# break
