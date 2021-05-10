#! /usr/bin/python3
import random
A = [9,3,9,3,9,7,9]
d = 0

while len(A) > 1:
    for i in range(0, len(A)):
        x = random.choice(A)
        #print('X = {}'.format(x))
        xi = A.index(x)
        for j in (0, len(A)):
            y = random.choice(A)
            #print('Y = {}'.format(y))
            yi = A.index(y)
        # if (xi == yi):
        #     d = 1

        oddX = xi
        oddY = yi
        if (x == y and x != 7 and y != 7):
            A.remove(A[xi])
            A.remove(A[yi])
            print('PARES REMOVIDOS: {} e {}'.format(x,y))
            print(A)
        else:
            print(A)
#print(x,y)
# if (x == y):
print(A)
print('FIM')

    


# def solution(A):
#     odd = 0
#     for i in A:
#         odd^=i
#     return odd
#     print(odd)

# solution(A)
