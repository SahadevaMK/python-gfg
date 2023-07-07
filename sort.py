list = [24,45,56,75,98,376,93,938,3]
newList = []

while list:
    min = list[0]
    for i in list:
        if (i > min):
            min = i
    newList.append(min)
    list.remove(min)

print(newList)
