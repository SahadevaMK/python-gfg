# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        j=0
        count1 = 0
        count2 =0
        arr1 = []
        arr2 = []
        temp1 = l1
        temp2 = l2
        while temp1 != None:
            count1+=1
            temp1=temp1.next    
        while temp2 != None:
            count2+=1
            temp2 = temp2.next
        temp3 = l1
        while i!=count1:
            arr1.append(temp3.val)
            i+=1
            temp3 = temp3.next
        temp4 = l2
        while j!=count2:
            arr2.append(temp4.val)
            j+=1
            temp4 = temp4.next
        arr1.reverse()
        arr2.reverse()
        
        result1 = int("".join(map(str,arr1)))
        result2 = int("".join(map(str,arr2)))
        final = result1+result2

        arrComp = [int(digit) for digit in str(final)]
        arrComp.reverse()
        dummyNode = ListNode(-1)
        cur = dummyNode
        for i in range(len(arrComp)):
            newNode = ListNode(arrComp[i])
            cur.next = newNode
            cur = cur.next
        return dummyNode.next
