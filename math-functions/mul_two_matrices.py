A = [
    [5,4,3],
    [2,4,6],
    [4,7,9]
]

B = [
    [3,2,4],
    [4,3,6],
    [2,7,5]
]

multiresult = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for m in range(len(A)):
    for n in range(len(B[0])):
        for o in range(len(B)):
            multiresult[m][n] += A[m][o] * B[o][n]

print("The multiplication result of matrix A and B is: ")
for res in multiresult:
    print(res)