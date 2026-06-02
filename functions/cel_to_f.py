# c = input("what's the tempurature int celcius? ")
def c_to_f(c): return (int(c) * 1.8 + 32)
while True:
	c = input("what's the temp in celcius? ")
	print(c_to_f(c))
	if c == ("quit"):
		break
