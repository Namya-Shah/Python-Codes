# Find the largest number
num = 0
arr = [24, 32, 41, 56, 32, 21]
for i in arr:
    if num < i:
        num = i
print(num)