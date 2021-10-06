#Python program to check if a number is positive, negative or zero.

def NumberCheck(a):
    if a > 0:
        print("The number is positive.")
    elif a < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

a = int(input("Enter number: "))
NumberCheck(a)