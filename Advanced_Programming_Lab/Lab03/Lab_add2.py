n = int(input("Enter the number of rows: "))
for i in range(n):
    coef = 1
    for j in range(1, n - i + 1):
        print(" ", end="")
    
    for j in range(0, i + 1):
        if j > 0:
            coef = coef * (i - j + 1) // j
        print(coef, end=" ")
    print()
#C(n, k) = n! / (k! * (n - k)!)