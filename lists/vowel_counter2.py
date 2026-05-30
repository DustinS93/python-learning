word = input("Type input to count vowels: ")
count = sum(1 for char in word.lower() if char in ("aeiou"))
print(count)
