def sum_under_100(numbers):
	total = 0					# Need a total to start adding from
	for i in numbers:				# For(loop through) each i (item) in the list of numbers 
		if i < 100:				# for every i if it is less than 100
			total = total + i		# then add it to the total that starts at 0
	return total					# return what the new total is and run through the for loop for each item 
print(sum_under_100([100, 200, 300, 1, 2, 3, 400]))
