conversion_k = 0.62137
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
choice = int(input("Enter your choice(1/2): "))
if choice == 1:
    kilometers = float(input("Enter kilometers: "))
    miles = kilometers * conversion_k
    print(miles)
elif choice == 2:
    miles = float(input("Enter miles: "))
    kilometers = miles/conversion_k
    print(kilometers)
else:
    print("You have entered wrong choice.")