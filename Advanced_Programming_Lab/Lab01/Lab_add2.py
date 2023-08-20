num = int(input("Enter a number: "))
sum = 0
temp = num
digits_in_num = len(str(num))
while temp > 0:
   n = temp % 10
   sum += n ** digits_in_num
   temp = temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")