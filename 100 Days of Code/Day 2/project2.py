# Tip Calculator

print("Welcome to the Tip Calculator")

a = float(input("What was the total bill? "))
b = int(input("What percentage tip you would like to give? 10, 12, or 15? "))
c = int(input("How many people to split the bill? "))

x = a * (b/100)
tip = ((a + x)/c)
y = round(tip, 2)

print(f"Each person should pay ${y}")