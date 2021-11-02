number = int(input("Enter the number: "))
print("The multiplication table of", number)
for count in range(1, 21):
    print(number, 'x', count, '=', number*count)