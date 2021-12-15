height = float(input("Enter height: "))
weight = float(input("Enter weight:" ))

a = weight / height ** 2

if a < 18.5:
    print(f"Your BMI is {a}, you are underweight.")
elif a < 25:
    print(f"Your BMI is {a}, you are normal.")
elif a < 30:
    print(f"Your BMI is {a}, you are overweight.")
elif a < 35:
    print(f"Your BMI is {a}, you are obese.")
else:
    print(f"Your BMI is {a}, you are clinically obese.")