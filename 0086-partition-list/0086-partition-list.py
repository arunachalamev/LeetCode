# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp1, temp2 = [], []
        while head:
            if head.val <x:
                temp1.append(head.val)
            else:
                temp2.append(head.val)
            
            head = head.next

        l1 = ListNode(0)
        sentinel = l1
        for x in temp1:
            newnode = ListNode(x)
            l1.next = newnode
            l1 = l1.next

        for x in temp2:
            newnode = ListNode(x)
            l1.next = newnode
            l1 = l1.next

        return sentinel.next            