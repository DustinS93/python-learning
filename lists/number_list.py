number_list = []
while True:
 print(number_list)
 get_numbers = input("Input Numbers: ")
 print("\nEnter Done When Finished")
 if get_numbers.lower() == "done":
  break
 else: 
  number_list.append(int(get_numbers))
print(max(number_list))
print(min(number_list))
print(sum(number_list) / len(number_list))
