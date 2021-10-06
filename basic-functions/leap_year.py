#Python program to know if year is leap or not
year = int(input("Enter year: "))
if year % 4 == 0:
    print("The year you entered is leap year")
else:
    print("The year you entered is not leap year")