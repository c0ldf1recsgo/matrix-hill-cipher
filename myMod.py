def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


# Driver Program 
# a = 15; m = 26
# print(modInverse(a, m))