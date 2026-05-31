def long_words(words):				
	result = []				# result must be called
	for i in words:		
		if len(i) > 4:			
			result.append(i)	# result called as an empty list gets appended with len(i) that is longer than 4
	return result				# first time writing function with both result and return, is return just a variable?
						# return can't be inside the loop
words = input("Type a sentence: ").split() 	# split the string from input, argument words for function must be a list here
print(long_words(words))
