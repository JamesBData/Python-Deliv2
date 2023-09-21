name = input("Hello, what is your name? ")
thislist = ["1. Apple $2", "2. Grape $1", "3. Orange $3"]
for x in thislist:
    print(x)

apple = 1
orange = 1
grape = 1
total_apples = 0
total_oranges = 0
total_grapes = 0
tax_rate = 0.050
bill = 0.0
tax = 0.0
total = 0.0
fruit_number = int(input("Welcome, " +name +"! Which Fruit would you like to buy?"))

if fruit_number == 1:
    bill = 2
    total_apples += 1
    print("You bought 1 apple at $2")
if fruit_number == 2:
    bill = 1
    total_grapes += 1
    print("You bought 1 grape at $1")
if fruit_number ==3:
    bill = 3
    total_oranges += 1
    print("You bought 1 orange at $3")

wants_another = input(f"Welcome, {name} would you like to buy another piece of fruit? y/n")

while wants_another == "y":
    fruit_number = int(input("Welcome," + name + "! Which Fruit would you like to buy?"))
    if fruit_number == 1:
        bill += 2
        total_apples += 1
        print("You bought 1 apple at $2")
    if fruit_number == 2:
        bill += 1
        total_grapes += 1
        print("You bought 1 grape at $1")
    if fruit_number == 3:
        bill += 3
        total_oranges += 1
        print("You bought 1 orange at $3")



    wants_another = input(f"Welcome, {name} would you like to buy another piece of fruit? y/n")
print(f"Receipt for {name}")

print("You bought: " +str(total_apples)+ " Apples.")
print("You bought: " +str(total_oranges)+ " Oranges.")
print("You bought: " +str(total_grapes)+ " Grapes.")
print("Your subtotal is: $" +str(bill))
tax = tax_rate * bill
print("Tax is: $" +str(tax))
total = tax + bill
print("Your total is: $" +str(total))






