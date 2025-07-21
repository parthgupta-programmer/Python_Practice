l1=[9,4,18,2,21,1,3,5,27]
max1=0
max2=0
for i in range(len(l1)):
    if(l1[i]>max1):
        max2=max1
        max1=l1[i]
    elif (l1[i]>max2 and l1[i]!=max1):
        max2=l1[i]
print("MAXIMUM ELEMENT : ",max1)
print("SECOND MAXIMUM ELEMENT : ",max2)