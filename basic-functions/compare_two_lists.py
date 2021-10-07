#Python program to compare two lists

list1 = [10,20,30,40,50]
list2 = [10,20,30,40,50]

a = set(list1)
b = set(list2)

if a == b:
    print("The two lists are equal")
else:
    print("The two lists are not equal")