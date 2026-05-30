word = input ("Input word to count vowels: ")
count = 0
for char in word.lower():
 if char in ("aeiou"):
  count += 1
print(count)
