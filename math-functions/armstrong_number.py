#Python program for finding Armstrong Number
#It has to be the same number after adding cubes of all the digits in the number
num = int(input("Enter a number: "))
sum = 0
temp = num

while temp>0:
    digit = temp%10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")