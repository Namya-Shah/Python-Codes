def add(x,y):
    return x + y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter your choice(1/2/3/4): ")
if choice == '1':
    print("Addition of", a, "and", b, "is", add(a,b))
elif choice == '2':
    print("Subtract of", a, "and", b, "is", sub(a,b))
elif choice == '3':
    print("Multiply of", a, "and", b, "is", mul(a,b))
elif choice == '4':
    print("Division of", a, "and", b, "is", div(a,b))
else:
    print("You have entered an incorrect choice")