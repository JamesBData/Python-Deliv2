name = input("Hello, what is your name? ")
thislist = ["1. Apple $2", "2. Grape $1", "3. Orange $3"]
for x in thislist:
    print(x)

fruit_number = input("Welcome, " +name +"! Which Fruit would you like to buy?")

if fruit_number == 1:
    bill = 2
    print("You bought 1 apple at $2")
if fruit_number == 2:
    bill = 1
    print("You bought 1 grape at $1")
if fruit_number ==3:
    bill = 3
    print("You bought 1 orange at $3")

wants_another = input("Would you like to buy another piece of fruit? y/n")

while wants_another == "y":
  input("Welcome," + name + "! Which Fruit would you like to buy?")
  if fruit_number == 1:
        bill = 2
        print("You bought 1 apple at $2")
  if fruit_number == 2:
        bill = 1
        print("You bought 1 grape at $1")
  if fruit_number == 3:
        bill = 3
        print("You bought 1 orange at $3")
  input(f"{wants_another}")
else:
    print(f"Receipt for {name}")


