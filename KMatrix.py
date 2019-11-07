# import LMatrix
# import UMatrix

# n = 3

# L = LMatrix.LGen(n, n)
# U = UMatrix.UGen(n, n)
# LMatrix.printMat(L)
# UMatrix.printMat(U)

# result = [[sum(a * b for a, b in zip(L_row, U_col))  
#                         for U_col in zip(*U)] 
#                             for L_row in L]

# for r in result: 
#     print(r)

a = 11
m = 26
from myMod import modInverse
if a < 0:
    print(modInverse(a%m, m))
else:
    print(modInverse(a,m))