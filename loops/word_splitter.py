sentance = input("Type a sentance: ")
word_list = sentance.split()
for i, word_list in enumerate(word_list, start = 1):
 print(f"{i}. {word_list}")
