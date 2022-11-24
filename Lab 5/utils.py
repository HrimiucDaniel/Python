def prime_number(i):
  for index in range(2, int(i/2)):
    if i % index == 0:
      return False
  return True

def process_item(x):
  y = int(x)
  while True:
    if prime_number(y) == True:
      return y
    y += 1

if __name__ == "__main__":
  number = input("Enter number: ")
  print(process_item(number))
  print("Salut")