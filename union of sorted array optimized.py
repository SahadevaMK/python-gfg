a = [1,2,3,4,5]
b=[1,2,6,7,8]

hs = set()
c=[]

for i in range(0,5):
    hs.add(a[i])
for i in range(0,5):
    c.append(a[i])
for i in range(0,5):
    if b[i] not in hs:
        c.append(b[i])
y = c.sort()

print(c)
