
shopping_list = []
while True:
 print("\nShopping List:", shopping_list)
 print("1. Add item")
 print("2. Remove Item")
 print("3. Quit")
 choose_option = input("Choose an option: 1. 2. 3. ")

 if choose_option == "1":
  print("\nAdd Item:")
  added_item = input()
  shopping_list.append(added_item)
 elif choose_option == "2":
  print("\nChoose Item to Remove: ")
  item_to_remove = int(input()) - 1
  shopping_list.pop(item_to_remove)
 elif choose_option == "3":
  print("Goodbye!")
  break  
