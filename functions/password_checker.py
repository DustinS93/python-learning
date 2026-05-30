while True:
 password = input("Insert Password ")
 if len(password) < 8:
  print(f"Passord needs to be longer than 8 characters, {password}")
 elif password.isalpha():
  print(f"Password must contain atleast 1 number, {password}")
 else:
  print("Password Accepted")
  break
