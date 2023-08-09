l1 = [2,5,8,12,4,6,87,32,65]
l2 = [1,6,3,90,4,5,32,4]
l3=[]
for i in l1:
    if i%2!=0:
        l3.append(i)
for j in l2:
    if j%2==0:
        l3.append(j)
print(l3)
