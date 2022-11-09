import utils

while True:
  number = input("Enter number: ")
  if number == "q":
    break
  print(utils.process_item(number))
  