m = int(input("enter m: "))
n = int(input("enter n: "))
print("prime no. b/w", m, "and", n, "are:")
for num in range(m, n + 1):
   if num > 1:
       for i in range(2, int(num/2)):
           if (num % i) == 0:
               break
       else:
           print(num)