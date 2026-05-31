number = int(input("What's your Fizz Buzz guess? \nType a number: ")) # Number input is called and converted to int in one line 
if number % 3 == 0 and number % 5 == 0: # Check both first because the first one that is true stops the program never getting to both 3 and 5 modulo
	print("FizzBuzz!!!") # The % modulo is checking the remainder, if the remainder == 0 that means the number is divisible with no remainder
elif number % 3 == 0:
	print("Buzz..")
elif number % 5 == 0:
	print("Fizz..")
else:
	print(number)
