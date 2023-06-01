class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        pos = []
        neg = []
        c=0
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        a = pos+neg
        for i in a:
            arr[c] = i
            c+=1
