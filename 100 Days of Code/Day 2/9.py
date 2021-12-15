age = int(input("What is your current age?"))

a = 90 * 365
b = 90 * 52
c = 90 * 12

x = age * 365
y = age * 52
z = age * 12

days = a - x
weeks = b - y
months = c - z
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
