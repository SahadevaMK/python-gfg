## prime number in a range
endd = int(input('enter the number'))
for i in range (1,endd):
    count = 0
    for j in range(1,i+1):
        count = count+1
    if(count==2):
        print(i,end=' ')

