name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
expected_age = 50

if age < expected_age:
    remaining_years = expected_age - int(age)
    print(f"Hello {name}, you will be {expected_age} in {remaining_years} years.")
else:
    print("You are already above 50.")