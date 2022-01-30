# importing libraries
import math

# greeting
print("Welcome to Financial Calculator!!!")

# all calculators listing
print("1. Compound Interest Calculator")
print("2. VAT Calculator")
print("3. Simple Interest Calculator")
print("4. GST Calculator")
print("5. Future Value")
print("6. Cummulative Annual Growth Rate")
print("7. Net Income Calculator")
print("8. Accounting Equation")
print("9. Cost of goods sold calculator")
print("10. Break-even point calculator")
print("11. Return on Investment")
print("12. Profit Margin")
print("13. Current Ratio")
print("14. Markup Percentage")
print("15. Inventory Shrinkage Calculator")
print("16. EBIDTA Calculator")
choice = input("Enter your choice: ")

# compound interest calculator
if choice == "1":
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

elif choice == "2":
    # taking user input for amount and vat %
    p = int(input("Enter amount: "))
    vat = int(input("Enter rate of vat (%): "))
    vat_value = p * (vat/100)
    a = p + vat_value
    
    # printing out functions
    print("Your Net Amount is", p)
    print("Your VAT Value is", vat_value)
    print("Your Total Amount is", a)

elif choice == "3":
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

elif choice == "4":
    # taking input for initial amount and gst rate
    gst = int(input("Enter GST Amount: "))
    rate = int(input("Enter GST rate (%): "))
    
    # calculating gst amount
    r = rate/100
    gst_amount = r * gst
    print('Your GST Amount is', gst_amount)
    total_amount = gst + gst_amount
    print('Your Total GST Amount is', total_amount)

elif choice == "5":
    print("1. Future Value using Simple Interest")
    print("2. Future Value using Compound Interest")
    pv = int(input("Enter Present Value: "))
    r = int(input("Enter Rate of Interest: "))
    t = int(input("Enter time period in years: "))
    choice = input("Enter your choice: ")
    if choice == "1":
        # F.V. = P.V. (1 + (R x T))
        fv = pv * (1 + (r * t))
        print(fv)
    elif choice == "2":
        # F.V. = P.V. (1 + r)**t
        fv = pv * ((1 + r)**t)
        print(fv)
    else:
        print("You have entered incorrect choice.")
    
elif choice == "6":
    fv = int(input("Enter future value: "))
    pv = int(input("Enter present value: "))
    n = int(input("Number of periods: "))
    '''
    r = (FV/PV)**(1/n)-1
    '''
    r = ((fv/pv)**(1/n)) - 1
    print("Your CAGR is", r)

elif choice == "7":
    x = float(input("Enter your Revenue: "))
    y = float(input("Enter your Expenses: "))
    
    # NET INCOME FORMULA  = REVENUE - EXPENSES
    z = x - y
    print("Your net income is", z)

elif choice == "8":
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

elif choice == "9":
    # COGS = BEGINNING INVENTORY + PURCHASES DURING THE PERIOD - ENDING INVENTORY
    x = float(input("Enter your Beginning Inventory: "))
    y = float(input("Enter your Purchases during the period: "))
    z = float(input("Enter your Ending Inventory: "))
    a = x + y - z
    print("Your Cost of Goods Sold are:", a)
    
elif choice == "10":
    # BREAK-EVEN POINT = FIXED COSTS / (SALES PRICE PER UNIT - VARIABLE COSTS PER UNIT)
    x = float(input("What are your Fixed Costs? "))
    y = float(input("What is your Sales Price? "))
    z = float(input("What are your Variable Costs Per Unit? "))
    a = x / (y - z)
    print("Your Break-Even Point is", a)
    
elif choice == "11":
    x = float(input("Enter your Investment Gain: "))
    y = float(input("Enter your Cost of Investment: "))
    # ROI = [(INVESTMENT GAIN - COST OF INVESTMENT) / COST OF INVESTMENT] * 100
    z = ((x-y)/y) * 100
    print("Your Return of Investment (ROI) is", z)

elif choice == "12":
    x = int(input("Enter your Net Income: "))
    y = int(input("Enter your Revenue: "))
    # PROFIT MARGIN = (NET INCOME / REVENUE) * 100
    z = (x/y)*100
    print("Your Profit Margin is", z)
    
elif choice == "13":
    x = int(input("Enter your Current Assets: "))
    y = int(input("Enter your Current Liabilities: "))
    # CURRENT RATIO = CURRENT ASSETS / CURRENT LIABILITIES
    z = x/y
    print("Your Current Margin is", z)
    
elif choice == "14":
    x = int(input("Enter your Revenue: "))
    y = int(input("Enter your Costs of Good Sold (COGS): "))
    # MARKUP PERCENTAGE = [(REVENUE - COGS) / COGS]*100
    z = ((x - y)/y)*100
    print("Your Markup Percentage is", z)
    
elif choice == "15":
    x = int(input("Enter your Recorded Inventory: "))
    y = int(input("Enter your Actual Inventory: "))
    # INVENTORY SHRINKAGE = [(RECORDED INVENTORY - ACTUAL INVENTORY) / RECORDED INVENTORY] * 100
    z = ((x-y)/x)*100
    print("Your Inventory Shrinkage is", z)
    
elif choice == "16":
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
    print("Coming Soon.")