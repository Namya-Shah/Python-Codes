list1 = [10,20,30,40,50]
print("Current numbers list:", list1)

n = int(input("Enter the number you want to: "))
index = int(input("Enter the position you want to insert: "))

list1.insert(index, n)
print('Updated numbers list: ', list1)