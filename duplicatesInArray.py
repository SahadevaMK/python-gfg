a =[2,3,1,2,3]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            print(a[i])
print(len(a))
