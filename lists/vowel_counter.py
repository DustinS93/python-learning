word = input ("Input word to count vowels: ") 
count = 0                            # counter starts at zero
for char in word.lower():            # loop char in word.lower - converts to lowercase
 if char in ("aeiou"):               # if any char ("aieou") is there              
  count += 1                         # add one to counter
print(count)
