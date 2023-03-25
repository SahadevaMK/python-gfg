## sum of odd and even numbers

x = int (input('enter the num'))
esum =0
osum =0
for i in range(x):
    if (i%2==0):
        esum = esum+i
    elif(i%2 != 0):
        osum=osum+i
print(esum)
print(osum)
