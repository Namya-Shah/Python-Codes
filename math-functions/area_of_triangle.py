a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))
c = float(input("Enter length of side C: "))

s = ((a+b+c)/2)

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of Triangle is", area)