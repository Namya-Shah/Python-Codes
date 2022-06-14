from numpy import exp2


exp = []
stopped = False

while not stopped:
    e = int(input("Enter the expense (type 0 to stop): "))
    if e != 0:
        exp.append(e)
    else:
        stopped = True

print(exp)
print("TOTAL EXPENSES: ", sum(exp))
print("MAXIMUM EXPENSES:", max(exp))
print("MINIMUM EXPENSES:", min(exp))