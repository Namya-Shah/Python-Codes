# importing libraries
import math

# greeting
print("Welcome to Financial Calculator!!!")

# all calculators listing
print("1. Compound Interest Calculator")
print("2. VAT Calculator")
print("3. Simple Interest Calculator")
print("4. GST Calculator")
a = input("Enter your choice: ")

# compound interest calculator
if a == "1":
    p = int(input("Enter Principal Amount: "))
    x = int(input("Enter Annual Interest Rate (%): "))
    t = int(input("Enter Period (in years): "))
    # Compound Interest Formula
    # C.I. = P(1+r/n)**n - P
    # Total Accumulated Amount = P(1+r/n)**n
    r = x/100
    
    a = p*(1+r)**t
    ci = a - p
    print("Your Compound Interest Amount is", round(ci,2))
    print("Your Total Accumulated Amount is", round(a,2))

elif a == "2":
    # taking user input for amount and vat %
    p = int(input("Enter amount: "))
    vat = int(input("Enter rate of vat (%): "))
    vat_value = p * (vat/100)
    a = p + vat_value
    
    # printing out functions
    print("Your Net Amount is", p)
    print("Your VAT Value is", vat_value)
    print("Your Total Amount is", a)

elif a == "3":
    # taking input for principal amount, rate and time period
    p = int(input("Enter principal amount: "))
    r = int(input("Enter rate of interest (%): "))
    t = int(input("Enter time period (in years): "))
    
    # calculating simple interest
    i = p*(r/100)*t
    print("Your Simple Interest Amount is", i)
    
    # printing total amount including simple interest
    a = p + i
    print("Your Total Amount is", a)

elif a == "4":
    # taking input for initial amount and gst rate
    gst = int(input("Enter GST Amount: "))
    rate = int(input("Enter GST rate (%): "))
    
    # calculating gst amount
    r = rate/100
    gst_amount = r * gst
    print('Your GST Amount is', gst_amount)
    total_amount = gst + gst_amount
    print('Your Total GST Amount is', total_amount)

elif a == "5":
    pass