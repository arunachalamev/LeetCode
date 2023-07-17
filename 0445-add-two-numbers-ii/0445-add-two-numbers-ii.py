# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def reverseList(l1):
            
            prev = None
            current = l1
            while current.next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            current.next = prev
            
            return current
        
        rev_l1 = reverseList(l1)
        rev_l2 = reverseList(l2)
        
        # while rev_l1:
        #     print (rev_l1.val)
        #     rev_l1 = rev_l1.next
        
        carry = 0
        ans = []
        while rev_l1 or rev_l2:
            # print (rev_l1.val, rev_l2.val)
            
            if rev_l1 and rev_l2:
                s = carry + rev_l1.val + rev_l2.val
            
            elif rev_l1:
                s = carry + rev_l1.val
            
            elif rev_l2: 
                s = carry + rev_l2.val
            
            s,carry = s%10, s//10
            
            if rev_l1:
                rev_l1 = rev_l1.next
            
            if rev_l2:
                rev_l2 = rev_l2.next
                
            ans.append (s)
        
        if carry:
            ans.append(carry)
        
        ans = ans[::-1]
        Sentinel = ListNode(0)
        head = Sentinel
        
        for d in ans:
            newNode = ListNode(d)
            head.next = newNode
            head = head.next

        
            
        return Sentinel.next
        