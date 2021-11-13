import math
print("Area Calculator")
print("1. 2D Shapes")
print("2. 3D Shapes")
a = input("Select type of shape(1/2): ")

if a == '1':
    print("Shapes:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Trapezium")
    print("6. Rhombus")
    b = input("Which shape area do you want to find: ")
    if b == '1':
        x = int(input("Enter side length: "))
        print(x**2)
    elif b == '2':
        x = int(input("Enter length: "))
        y = int(input("Enter breadth: "))
        print(x*y)
    elif b == '3':
        x = int(input("Enter radius: "))
        print((math.pi)*x**2)
    elif b == '4':
        x = int(input("Enter base: "))
        y = int(input("Enter perpendicular height: "))
        print(1/2*(x*y))
    elif b == '5':
        x = int(input("Enter length of parallel side 1: "))
        y = int(input("Enter length of parallel side 2: "))
        h = int(input("Enter height of the trapezium: "))
        print(h/2*(x+y))
    elif b == '6':
        x = int(input("Enter length of the base: "))
        y = int(input("Enter length of height: "))
        print(x*y)
    else:
        print("You have entered wrong choice.")
elif a == '2':
    print("Shapes:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Sphere")
    print("4. Hemisphere")
    print("5. Cylinder")
    print("6. Cone")
    b = input("Which shape area do you want to find: ")
    if b == '1':
        x = int(input("Enter side length: "))
        print(6*(x**2))
    elif b == '2':
        print("1. Lateral Surface Area")
        print("2. Total Surface Area")
        c = input("Which type of area you want to find: ")
        if c == '1':
            x = int(input("Enter length: "))
            y = int(input("Enter width: "))
            z = int(input("Enter height: "))
            print(2*z*(x + y))
        elif c == '2':
            x = int(input("Enter length: "))
            y = int(input("Enter width: "))
            z = int(input("Enter height: "))
            print(2*(x*y + y*z + z*x))
        else:
            print("You have entered a wrong choice.")
    elif b == '3':
        x = int(input("Enter radius: "))
        print(4*(math.pi)*(x**2))
    elif b == '4':
        print("Which type of area you want to find: ")
        print("1. Curved Surface Area")
        print("2. Total Surface Area")
        c = input("Enter your choice: ")
        if c == '1':
            x = int(input("Enter radius: "))
            print(2*(math.pi)*x**2)
        elif c == '2':
            x = int(input("Enter radius: "))
            print(3*(math.pi)*x**2)
        else:
            print("You have entered wrong choice.")
    elif b == '5':
        x = int(input("Enter radius: "))
        y = int(input("Enter height: "))
        print(2*(math.pi)*x*(x+y))
    elif b == '6':
        x = int(input("Enter radius: "))
        y = int(input("Enter perpendicular length: "))
        print((math.pi)*x*(y+x))
    else:
        print("You have entered wrong choice.")
            
        
    
