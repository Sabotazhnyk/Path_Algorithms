A = {str([1,2]):1,str([3,4]):2}
for i in A:
    if i == str([1,2]): print("yes")
# A.pop(str([1,2]))
b = (A.keys())
B = {(list(A.keys())[0]): A[list(A.keys())[0]]}
A.pop(list(A.keys())[0])

A.update(B)

print(A)