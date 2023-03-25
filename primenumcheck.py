## prime number check 
num = int(input('enter the number'))
for i in range(2,num):
    if (num%i==0):
        print('not prime')
        break;
else:
     print('prime')

