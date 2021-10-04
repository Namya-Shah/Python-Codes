a = float(input("Enter temperature in Celsius/Fahrenheit: "))
print("1. Celsius to Farenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice(1/2): "))

if choice == 1:
    fahrenheit = a*1.8+32
    print(fahrenheit)
elif choice == 2:
    celsius = a-32/1.8
    print(celsius)
'''
else:
    print("You have inputed wrong choice")'''