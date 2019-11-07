import random

n = 3
def UGen(rol, col):
    U = []
    subU = []
    for i in range(rol):
        for j in range(col):
            subU.append(random.randint(0,10))
        U.append(subU)
        subU = []
    for i in range(rol):
        for j in range(i):
            U[i][j] = 0
    return U

def printMat(U):
    for i in range(len(U)):
        print(U[i])
    print("\n")

# def main():
#     U = UGen(n, n)
#     printMat(U)

# if __name__ == "__main__":
#     main()