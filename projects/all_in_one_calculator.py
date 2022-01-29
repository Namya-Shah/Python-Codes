import math

print("1. Calculator")
print("2. Area Calculator")
print("3. Volume Calculator")
print("4. Length Converter")
print("5. Speed Converter")
print("6. Temperature")
print("7. Weight Converter")
print("8. Tip")
print("9. Body Mass Index Calculator")
print("10. Age")
print("11. Prime Checker")
print("12. Angle")
print("13. Cooking")
print("14. Force")
print("15. Fuel")
print("16. Numeric Base")
print("17. Power")
print("18. Pressure")
print("19. Torque")
print("20. Ohm's Law")
print("21. Cummulative Annual Growth Rate")
print("22. Quadratic Equation Solver")
print("23. x^y calculator")
print("24. Pythagoreas Theorem")
print("25. Net Income Formula")
print("26. Accounting Equation")
print("27. Cost of goods sold formula")
print("28. Break-even point formula")
print("29. Return on Investment")
print("30. Profit Margin")
print("31. Current Ratio")
print("32. Markup Percentage")
print("33. Inventory Shrinkage Formula")

choice = input("What do you want to use (1/33)? ")

# 1. Calculator
if choice == '1':
    def add(x,y):
        return x+y
    
    def sub(x,y):
        return x-y
    
    def mul(x,y):
        return x*y
    
    def div(x,y):
        return x/y
    
    def percent(x,y):
        return x/y * 100
    
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percent")
    option = input("Enter your choice: ")
    
    if option == '1':
        print("The addition of", a, "and", b, "is", add(a,b))
    elif option == '2':
        print("The subtraction of", a, "and", b, "is", sub(a,b))
    elif option == '3':
        print("The multiplication of", a, "and", b, "is", mul(a,b))
    elif option == '4':
        print("The division of", a, "and", b, "is", div(a,b))
    elif option == '5':
        print("The percentage of", a, "and", b, "is", percent(a,b))
    else:
        print("You have entered incorrect choice")

# 2. Area Calculator
elif choice == '2':
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
        print("7. Pentagon")
        print("8. Hexagon")
        print("9. Circle Arc")
        print("10. Ellipse")
        
        b = input("Which shape area do you want to find: ")
        if b == '1':
            # Area of Square
            x = int(input("Enter side length: "))
            print("Area of Square is", x**2)
        elif b == '2':
            # Area of Rectangle
            x = int(input("Enter length: "))
            y = int(input("Enter breadth: "))
            print("Area of Rectangle is", x*y)
        elif b == '3':
            # Area of Circle
            x = int(input("Enter radius: "))
            print("Area of Circle is", (math.pi)*x**2)
        elif b == '4':
            # Area of Triangle
            x = int(input("Enter base: "))
            y = int(input("Enter perpendicular height: "))
            print("Area of Triangle is", 1/2*(x*y))
        elif b == '5':
            # Area of Trapezium
            x = int(input("Enter length of parallel side 1: "))
            y = int(input("Enter length of parallel side 2: "))
            h = int(input("Enter height of the trapezium: "))
            print("Area of Trapezium is", h/2*(x+y))
        elif b == '6':
            # Area of Rhombus
            x = int(input("Enter length of the base: "))
            y = int(input("Enter length of height: "))
            print("Area of Rhombus is", x*y)
        elif b == '7':
            # Area of Pentagon
            x = int(input("Enter side length: "))
            print("Area of Pentagon is", (x**2)*1.72)
        elif b == '8':
            # Area of Hexagon
            x = int(input("Enter side length: "))
            print("Area of Hexagon is", (x**2)*2.6)
        elif b == '9':
            # Area of Circle Arc
            x = int(input("Enter radius: "))
            y = int(input("Enter angle: "))
            z = math.pi*(x**2)*(y/360)
            print("Area of Circle Arc is", z)
        elif b == '10':
            # Area of Ellipse
            x = int(input("Enter radius: "))
            y = int(input("Enter radius: "))
            z = math.pi*x*y
            print("Area of Ellipse is", z)
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
        print("7. Pyramid")
        print("8. Pyramid Frustum")
        print("9. Cone Frustum")
        print("10. Ellipsoid")
        b = input("Which shape area do you want to find: ")
        if b == '1':
            # Area of Cube
            x = int(input("Enter side length: "))
            print("Area of Cube is", 6*(x**2))
        elif b == '2':
            # Area of Cuboid
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            c = input("Which type of area you want to find: ")
            if c == '1':
                # Lateral Surface Area
                x = int(input("Enter length: "))
                y = int(input("Enter width: "))
                z = int(input("Enter height: "))
                print("Area of Lateral Surface Area of Cuboid is", 2*z*(x + y))
            elif c == '2':
                # Total Surface Area
                x = int(input("Enter length: "))
                y = int(input("Enter width: "))
                z = int(input("Enter height: "))
                print("Area of Total Surface Area of Cuboid is", 2*(x*y + y*z + z*x))
            else:
                # If you have entered more than 2 in your choice
                print("You have entered a wrong choice.")
        elif b == '3':
            # Area of Sphere
            x = int(input("Enter radius: "))
            print("Area of Sphere is", 4*(math.pi)*(x**2))
        elif b == '4':
            # Area of Hemisphere
            print("Which type of area you want to find: ")
            print("1. Curved Surface Area")
            print("2. Total Surface Area")
            c = input("Enter your choice: ")
            if c == '1':
                # Curved Surface Area
                x = int(input("Enter radius: "))
                print("Area of Curved Surface Area of Hemisphere is", 2*(math.pi)*x**2)
            elif c == '2':
                # Total Surface Area
                x = int(input("Enter radius: "))
                print("Area of Total Surface Area of Hemisphere is", 3*(math.pi)*x**2)
            else:
                print("You have entered wrong choice.")
        elif b == '5':
            # Area of Cylinder
            x = int(input("Enter radius: "))
            y = int(input("Enter height: "))
            print("Area of Cylinder is", 2*(math.pi)*x*(x+y))
        elif b == '6':
            # Area of Cone
            x = int(input("Enter radius: "))
            y = int(input("Enter perpendicular length: "))
            print("Area of Cone is", (math.pi)*x*(y+x))
        elif b == '7':
            # Area of Pyramid
            x = int(input("Enter side length: "))
            y = int(input("Enter height: "))
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            num = input("Enter your choice: ")
            if num == '1':
                z = 2*x*math.sqrt((y**2)+(((x/2)**2)))
                print("Area of Lateral Surface Area of Pyramid is", z)
            elif num == '2':
                x = int(input("Enter side length: "))
                print("Area of Total Surface Area of Pyramid is", 32.02+(x**2))
            else:
                print("You have entered wrong choice.")
        elif b == '8':
            # Area of Pyramid Frustum
            x = int(input("Enter side length A: "))
            y = int(input("Enter side length B: "))
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            num = input("Enter your choice: ")
            if num == '1':
                z = int(input("Enter height: "))
                n = 2*(x+y)*math.sqrt((z**2)+((y-x/2)**2))
            elif num == '2':
                print("Area of Total Surface Area of Pyramid Frustum is", 50.25+(x**2)+(y**2))
            else:
                print("You have entered wrong choice.")
        elif b == '9':
            # Area of Cone Frustum
            x = int(input("Enter side length A: "))
            y = int(input("Enter side length B: "))
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            num = input("Enter your choice: ")
            if num == '1':
                z = int(input("Enter height: "))
                s = math.sqrt(((y-x)**2) + (z**2))
                la = math.pi * (x + y) * s
                print("Area of Lateral Surface Area of Cone Frustum is", la)
            elif num == '2':
                n1 = 80.1 + math.pi*(x**2) + math.pi*(y**2)
                print("Area of Total Surface Area of Cone Frustum is", n1)
            else:
                print("You have entered wrong choice.")
        elif b == '10':
            # Area of Ellipsoid
            x = int(input("Enter radius A: "))
            y = int(input("Enter radius B: "))
            z = int(input("Enter radius C: "))
            area = (4 * 3.141592653 * pow((pow(x * y, 1.6) + pow(x * z, 1.6) + pow(y * z, 1.6)) / 3, 1 / 1.6))
            print("Area of Ellipsoid is", area)
        else:
            print("You have entered wrong choice.")

# 3. Volume Calculator
elif choice == '3':
    print("Shapes:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Sphere")
    print("4. Hemisphere")
    print("5. Cylinder")
    print("6. Cone")
    print("7. Pyramid")
    print("8. Pyramid Frustum")
    print("9. Cone Frustum")
    print("10. Ellipsoid")
    print("11. Sphere Segment")
    b = input("Which shape area do you want to find: ")
    if b == '1':
        # Volume of Square
        x = int(input("Enter side length: "))
        print("Volume of Square is", x**3)
    elif b == '2':
        # Volume of Cuboid
        x = int(input("Enter side length A: "))
        y = int(input("Enter side length B: "))
        z = int(input("Enter side length C: "))
        print("Volume of Cuboid is", x*y*z)
    elif b == '3':
        # Volume of Sphere
        x = int(input("Enter radius: "))
        y = (4*math.pi*(x**3))/3
        print("Volume of Sphere is", y)
    elif b == '4':
        # Volume of Hemisphere
        x = int(input("Enter radius: "))
        y = int(input("Enter height: "))
        V = (3*math.pi*y*((x**2)+(y**2)))/6
        print("Volume of Hemisphere is", V)
    elif b == '5':
        # Volume of Cylinder
        x = int(input("Enter side length: "))
        y = int(input("Enter height: "))
        V = math.pi*(x**2)*y
        print("Volume of Cylinder is", V)
    elif b == '6':
        # Volume of Cone
        x = int(input("Enter radius: "))
        y = int(input("Enter height: "))
        V = (math.pi*(x**2)*y)/3
        print("Volume of Cone is", V)
    elif b == '7':
        # Volume of Pyramid
        x = int(input("Enter side length: "))
        y = int(input("Enter height: "))
        V = (x**2)*(y/3)
        print("Volume of Pyramid is", V)
    elif b == '8':
        # Volume of Pyramid Frustum
        x = int(input("Enter side length A: "))
        y = int(input("Enter side length B: "))
        z = int(input("Enter height: "))
        V = (((x**2) + x*y + (y**2)) * z)/3
        print("Volume of Pyramid Frustum is", V)
    elif b == '9':
        # Volume of Cone Frustum
        x = int(input("Enter side length A: "))
        y = int(input("Enter side length B: "))
        z = int(input("Enter height: "))
        V = (math.pi*z*((x**2) + x*y + (y**2)))/3
        print("Volume of Cone Frustum is", V)
        
    elif b == '10':
        # Volume of Ellipsoid
        x = int(input("Enter radius A: "))
        y = int(input("Enter radius B: "))
        z = int(input("Enter radius C: "))
        V = (4*math.pi*x*y*z)/3
        print("Volume of Ellipsoid is", V)
        
    elif b == '11':
        # Volume of Sphere Segment
        x = int(input("Enter radius A: "))
        y = int(input("Enter radius B: "))
        z = int(input("Enter height: "))
        V = (3*math.pi*z*(3*(x**2) + 3*(y**2) + z**2))/6
        print("Volume of Sphere Segment is", V)
        
    else:
        print("You have entered incorrect choice.")

# 4. Length Converter (m -> km, inch, foot, mile, centimeter, yard)
elif choice == '4':
    x = int(input("Enter length (in m): "))
    '''
    m = x/1000 km
    m = x * 39.37 inch
    m = x * 3.281 foot
    m = x/1852 mile
    m = x * 100 cm
    m = x * 1.094 yard
    '''
    print("Converted value of length is", x/1000, "km")
    print("Converted value of length is", x*39.37, "inch")
    print("Converted value of length is", x*3.281, "foot")
    print("Converted value of length is", x/1852, "mile")
    print("Converted value of length is", x*100, "cm")
    print("Converted value of length is", x*1.094, "yard")

# 5. Speed Converter (m/s -> km/hr, foot/s, mile/hr)
elif choice == '5':
    x = int(input("Enter speed (in m/s): "))
    '''
    m/s = x * 3.6 km/hr
    m/s = x * 3.281 foot/s
    m/s = x * 2.237 miles/hr
    '''
    print("Converted value of speed is", x*3.6, "km/hr")
    print("Converted value of speed is", x*3.281, "foot/s")
    print("Converted value of speed is", x*2.237, "miles/hr")

# 6. Temperature (C -> F, K)
elif choice == '6':
    x = int(input("Enter temperature (in Celsius): "))
    '''
    C = x + 273 K
    C = x * (9/5) + 32 F
    '''
    print("Converted value of temperature is", x+273, "K")
    print("Converted value of temperature is", x*(9/5)+32, "F")

# 7. Weight (g -> kg, metric ton, ounce, pound)
elif choice == '7':
    x = int(input("Enter weight (in g): "))
    '''
    g = x / 1000 kg
    g = x / 1000000 tonne
    g = x / 28.35 ounce
    g = x / 454 pound
    '''
    print("Converted value of weight is", x/1000, "kg")
    print("Converted value of weight is", x/1000000, "tonne")
    print("Converted value of weight is", x/28.35, "ounce")
    print("Converted value of weight is", x/454, "pound")

# 8. Tip (Bill, People, Tip%)
elif choice == '8':
    bill = input("Enter value of bill: ")
    people = int(input("Enter number of people: "))
    tip = int(input("Enter tip value (in %): "))
    x = bill*(tip/100)
    y = bill + x
    print("Final bill is", y)
    cpp = y/people
    print("Cost per person is", cpp)
    print("Tip amount is", x)

# 9. Body Mass Index (Height(cm), Weight(kg))
elif choice == '9':
    x = float(input("Enter your height: "))
    y = float(input("Enter your weight: "))
    bmi = 703 * y/(x ** 2)
    print(bmi)
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5<bmi>24.9:
        print("You are normal")
    elif 25.0<bmi>29.9:
        print("You are overweight")
    else:
        print("You are very overweight")

# 10. Age (Birthdate, Today Date)
elif choice == '10':
    from datetime import datetime, date

    print("Your date of birth (dd mm yyyy)")
    date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    age = calculate_age(date_of_birth)

    print(age)

# 11. Prime Checker
elif choice == '11':
    def PrimeChecker(a):
        if a>1:
            for j in range(2, int(a/2)+1):
                if (a % j) == 0:
                    print(a, "is not a prime number")
                break
            else:
                print(a, "is prime number")
        else:
            print(a, "is a prime number")

    a = int(input("Enter number: "))
    PrimeChecker(a)

# 12. Angle (Radian -> Degree, Minute, Second)
elif choice == '12':
    x = input("Enter angle (in radian): ")
    '''
    radian = radian measure * (180/pi)
    radian = radian measure * (60*180)/pi
    radian = radian measure * (3600*180)/pi
    '''
    print("Converted value of angle is", x*(180/math.pi), "degrees")
    print("Converted value of angle is", x*(60*180)/math.pi,'"')
    print("Converted value of angle is", x*(3600*180)/math.pi,"'")

# 13. Cooking (ml -> US Teaspoon, US Tablespoon, US Cup)
elif choice == '13':
    x = int(input("Enter value of cooking (in ml): "))
    '''
    ml = x / 4.929 teaspoon
    ml = x / 14.787 tablespoon
    ml = x / 240 cup
    '''
    print("Converted value of cooking is", x/4.929, "teaspoon")
    print("Converted value of cooking is", x/14.787, "tablespoon")
    print("Converted value of cooking is", x/240, "cup")

# 14. Force (N -> Dyne, Kilogram, Pound)
elif choice == '14':
    x = input("Enter force (in N): ")
    '''
    force = x * 100000 dyne
    force = x / 9.81 kg
    force = x / 4.448 pound
    '''
    print("Converted value of force is", x*100000, "dyne")
    print("Converted value of force is", x/9.81, "kg")
    print("Converted value of force is", x*4.448, "pound")

# 15. Fuel (l/100km -> km/l, ,mile per US gallon)
elif choice == '15':
    x = int(input("Enter fuel value (in l/100km): "))
    '''
    l/100 km = 100/x km/l
    l/100 km = 100 * 3.785411784/1.609344 * litres
    '''
    print("Converted value of fuel is", 100/x, "km/l")
    print("Converted value of fuel is", (100*3.785411784)/(1.609344*x), "mpg")

# 16. Numeric Base (Binary -> Decimal)
elif choice == '16':
    x = input("Enter binary number: ")
    dec_number = int(x, 2)
    print('The decimal conversion is: ', dec_number)
    print(type(dec_number))

# 17. Power (Watt -> kilowatt, horsepower)
elif choice == '17':
    x = int(input("Enter value of power (in watt): "))
    '''
    watt = x/1000 kilowatt
    watt = x/745.699872 horsepower
    '''
    print("Converted value of power is", x/1000, "kW")
    print("Converted value of power is", x/745.699872, "hp")

# 18. Pressure (atm -> bar, pascal, pound/inch^2)
elif choice == '18':
    x = int(input("Enter value of pressure (in atm): "))
    '''
    atm = x * 1.013 bar
    atm = x * 101325 pascal
    atm = x * 14.696 pound/inch^2
    '''
    print("Converted value of pressure is", x*1.013, "bar")
    print("Converted value of pressure is", x*101325, "pascal")
    print("Converted value of pressure is", x*14.696, "pound/inch^2")

# 19. Torque (N-m -> kilogram force-meter, pound force-inch, pound force-foot)
elif choice == '19':
    x = int(input("Enter value of torque (in N-m): "))
    '''
    N-m = x / 9.807 kgf-m
    N-m = x * 8.851 poundf-inch
    N-m = x / 1.356 poundf-foot
    '''
    print("Converted value of torque is", x/9.807, "kgf-m")
    print("Converted value of torque is", x*8.851, "poundf-inch")
    print("Converted value of torque is", x/1.356, "poundf-foot")

# 20. Ohm's Law
elif choice == '20':
    print("What value you want to find?")
    print("1. Current")
    print("2. Resistance")
    print("3. Voltage")
    c = input("Enter your choice: ")
    '''
    V = IR
    '''
    if c == '1':
        a = int(input("Enter resistance: "))
        b = int(input("Enter voltage: "))
        z = b/a
        print("Current is", z)
    elif c == '2':
        a = int(input("Enter current: "))
        b = int(input("Enter voltage: "))
        z = b/a
        print("Resistance is", z)
    elif c == '3':
        a = int(input("Enter resistance: "))
        b = int(input("Enter current: "))
        z = a*b
        print("Voltage is", z)
    else:
        print("You have entered wrong choice.")

# 21. CAGR (Cummulative Annual Growth Rate)
elif choice == '21':
    fv = int(input("Enter future value: "))
    pv = int(input("Enter present value: "))
    n = int(input("Number of periods: "))
    '''
    r = (FV/PV)**(1/n)-1
    '''
    r = ((fv/pv)**(1/n)) - 1
    print("Your CAGR is", r)

# 22. Quadratic Equation Solver
elif choice == '22':
    import cmath
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    c = float(input("Enter c:"))

    d = (b**2)-(4*a*c)

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))

# 23. x^y calculator
elif choice == '23':
    x = int(input("Enter a number: "))
    y = int(input("Enter power: "))
    print("{} to the power of {}".format(x,y),"is",pow(x,y))

# 24. Pythagoreas Theorem
elif choice == '24':
    print("Which side you wish to find: ")
    print("1. Hypotenuse")
    print("2. Base")
    print("3. Perpendicular Height")
    option = input("What is your choice: ")
    if option == '1':
        x = int(input("Enter base length: "))
        y = int(input("Enter perpendicular height: "))
        z = math.sqrt(x**2 + y**2)
        print("Length of hypotenuse", z)
    elif option == '2':
        x = int(input("Enter hypotenuse length: "))
        y = int(input("Enter perpendicular height: "))
        z = math.sqrt(x**2 - y**2)
        print("Length of base", z)
    elif option == '3':
        x = int(input("Enter hypotenuse length: "))
        y = int(input("Enter base length: "))
        z = math.sqrt(x**2 - y**2)
        print("Length of perpendicular height", z)
    else:
        print("You have entered a incorrect choice")

# 25. Net Income Formula
elif choice == '25':
    x = float(input("Enter your Revenue: "))
    y = float(input("Enter your Expenses: "))
    
    # NET INCOME FORMULA  = REVENUE - EXPENSES
    z = x - y
    print("Your net income is", z)

# 26. Accounting Equation
elif choice == '26':
    print("1. Assets")
    print("2. Liabilities")
    print("3. Equity")
    a = input("Enter your choice: ")
    if a == '1':
        # ASSETS = LIABILITIES + EQUITY
        x = int(input("Enter your liabilities: "))
        y = int(input("Enter your equity: "))
        z = x + y
        print("Your Assets are", z)
    
    elif a == '2':
        # LIABILITIES = ASSETS - EQUITY
        x = int(input("Enter your assets: "))
        y = int(input("Enter your equity: "))
        z = x - y
        print("Your Liabilities are", z)
    
    elif a == '3':
        # EQUITY = ASSETS - LIABILITIES
        x = int(input("Enter your liabilities: "))
        y = int(input("Enter your assets: "))
        z = y - x
        print("Your Equity is", z)

# 27. Cost of goods sold formula
elif choice == '27':
    # COGS = BEGINNING INVENTORY + PURCHASES DURING THE PERIOD - ENDING INVENTORY
    x = float(input("Enter your Beginning Inventory: "))
    y = float(input("Enter your Purchases during the period: "))
    z = float(input("Enter your Ending Inventory: "))
    a = x + y - z
    print("Your Cost of Goods Sold are:", a)

# 28. Break-even point formula
elif choice == '28':
    # BREAK-EVEN POINT = FIXED COSTS / (SALES PRICE PER UNIT - VARIABLE COSTS PER UNIT)
    x = float(input("What are your Fixed Costs? "))
    y = float(input("What is your Sales Price? "))
    z = float(input("What are your Variable Costs Per Unit? "))
    a = x / (y - z)
    print("Your Break-Even Point is", a)

# 29. Return on Investment
elif choice == '29':
    x = float(input("Enter your Investment Gain: "))
    y = float(input("Enter your Cost of Investment: "))
    # ROI = [(INVESTMENT GAIN - COST OF INVESTMENT) / COST OF INVESTMENT] * 100
    z = ((x-y)/y) * 100
    print("Your Return of Investment (ROI) is", z)

# 30. Profit Margin
elif choice == '30':
    x = int(input("Enter your Net Income: "))
    y = int(input("Enter your Revenue: "))
    # PROFIT MARGIN = (NET INCOME / REVENUE) * 100
    z = (x/y)*100
    print("Your Profit Margin is", z)

# 31. Current Ratio
elif choice == '31':
    x = int(input("Enter your Current Assets: "))
    y = int(input("Enter your Current Liabilities: "))
    # CURRENT RATIO = CURRENT ASSETS / CURRENT LIABILITIES
    z = x/y
    print("Your Current Margin is", z)

# 32. Markup Percentage
elif choice == '32':
    x = int(input("Enter your Revenue: "))
    y = int(input("Enter your Costs of Good Sold (COGS): "))
    # MARKUP PERCENTAGE = [(REVENUE - COGS) / COGS]*100
    z = ((x - y)/y)*100
    print("Your Markup Percentage is", z)

# 33. Inventory Shrinkage Formula
elif choice == '33':
    x = int(input("Enter your Recorded Inventory: "))
    y = int(input("Enter your Actual Inventory: "))
    # INVENTORY SHRINKAGE = [(RECORDED INVENTORY - ACTUAL INVENTORY) / RECORDED INVENTORY] * 100
    z = ((x-y)/x)*100
    print("Your Inventory Shrinkage is", z)

# 34. EBIDTA Formula
elif choice == '34':
    print("1. Using Net Income")
    print("2. Using Operating Profit")
    option = input("Enter your choice: ")
    if option == '1':
        x = int(input("Enter your Net Income: "))
        y = int(input("Enter your Interest: "))
        z = int(input("Enter your Taxes: "))
        depreciation = int(input("Enter Depreciation Amount: "))
        amortization = int(input("Enter Amortization Amount: "))
        a = x + y + z + depreciation + amortization
        print("Your EBIDTA is", a)
    elif option == '2':
        x = int(input("Enter your Operating Profit: "))
        depreciation = int(input("Enter Depreciation Amount: "))
        amortization = int(input("Enter Amortization Amount: "))
        a = x + depreciation + amortization
        print("Your EBIDTA is", a)

else:
    print("You have entered incorrect choice.")