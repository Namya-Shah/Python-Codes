from datetime import date
import csv
from tracemalloc import stop

dt = date.today()
dt = dt.strftime('%d/%m/%Y')

filename = "expense.csv"
exp = []
stopped = False

with open(filename, 'a', newline="") as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input("What is the expense (type 0 to stop): "))
        if xp == 0:
            stopped = True
        else:
            csvwriter.writerow([dt, xp])
            exp.append(xp)
            
print("Your expenses are: ", exp)
print("Your total expenses: ", sum(exp))