exp = -1
total = 0
maxexp = 0
minexp = 0

while exp != 0:
    exp = int(input("What's the expense? (Press 0 to stop it)"))
    total = total + exp
    if exp>maxexp:
        maxexp = exp
    if exp<minexp:
        minexp = exp

e = list(str(exp))
print(e)

print("Your total expenditure is ", str(total))
print("Your maximum expenditure is", str(maxexp))
print("Your minimum expenditure is", str(minexp))