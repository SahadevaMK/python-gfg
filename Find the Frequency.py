#User function Template for python3

"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""
def findFrequency (arr, n, x):
    # Your Code Here
    c=0
    for i in range(0,n):
        if arr[i] == x:  c+=1
    return c
        

