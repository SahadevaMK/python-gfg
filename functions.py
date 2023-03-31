def tables(num):
    for i in range(10):
        i=i+1
        print(f"{num} X {i} = {num*i}")

def repeat (num):
    for i in range(11):
        print(f"this number made me repeat this {num} times")


print("1.tables\n 2.repeat ")
options = int (input('enter your options'))
num = int (input("enter the number"))

if (options == 1):
    tables(num)
elif (options == 2):
    repeat(num)
else:
    print('invalid option! TRY again')
