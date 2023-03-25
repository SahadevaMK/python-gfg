## reversre a number and check palindrome or not

num = int(input('enter the num to be reveresed'))

temp = num
rev = 0

while(num>0):
    dig = num%10
    rev = rev*10+dig
    num = num//10
    
print(rev)
if (rev == temp):
    print('the num is palindrome')
else:
    print('the num is not palindrome')
