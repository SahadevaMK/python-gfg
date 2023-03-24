## largest of three numbers

x=int(input('enter the first number'))
y=int(input('enter the second number'))
z=int(input('enter the third number'))

if (x>y and x>z):
    print( f"first num is greater than second number and third number")
elif(y>z and y>z):
    print(f"second number is greater than first number and third number")
else:
    print(f"third number is greater than first number and second number")
