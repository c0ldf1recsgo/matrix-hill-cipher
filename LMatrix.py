import random

n = 3
def LGen(rol, col):
    L = []
    subL = []
    for i in range(rol):
        for j in range(col):
            subL.append(random.randint(0,10))
        L.append(subL)
        subL = []
    for i in range(rol):
        for j in range(i+1,col):
            L[i][j] = 0
    return L

def printMat(L):
    for i in range(len(L)):
        print(L[i])
    print("\n")

# def main():
#     L = LGen(n, n)
#     printMat(L)

# if __name__ == "__main__":
#     main()