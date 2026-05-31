def reverse_word(word):  			# Function goes above everything eise - what is "everything" else called?
	if len(word) > 5:			# Gets the lengths of the word and checks if it's more than 5
		return word[::-1]		# Returns the word reversed 
	else:
		return word
while True:					# Loop function
	word = input("Type a word, if it's long enough I'll reverse it: ") # The word as an input that is used as the functions argument
	print(reverse_word(word))
	if word == "quit":			# If loop within the While loop, checks if the word is quit to stop program
		break
