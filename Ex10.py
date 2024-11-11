listA = [10, 20, 25, 30, 35]
listB = [40, 45, 60, 75, 90]
listC=[]

for val in listA :
    if(val%2!=0):
        listC.append(val)

for val in listB :
    if(val%2==0):
        listC.append(val)

for val in listC :
    print(val, end=" ")
