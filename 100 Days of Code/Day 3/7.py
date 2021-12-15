print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
a = input("Do you want to add pepporoni? Y or N ")
b = input("Do you want to add cheese? Y or N ")

print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")

print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")

print("Extra cheese for any size pizza: +$1")

if size == "S":
    if a == "Y":
        if b == "Y":
            print("Your total bill is $18")
        else:
            print("Your total bill is $17")
    else:
        print("Your total bill is $15")

if size == "M":
    if a == "Y":
        if b == "Y":
            print("Your total bill is $23")
        else:
            print("Your total bill is $22")
    else:
        print("Your total bill is $20")
        
if size == "L":
    if a == "Y":
        if b == "Y":
            print("Your total bill is $28")
        else:
            print("Your total bill is $27")
    else:
        print("Your total bill is $25")