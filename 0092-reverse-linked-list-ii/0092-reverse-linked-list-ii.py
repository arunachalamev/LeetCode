# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        temp = []
        curr = head
        count = 0
        while curr:
            count += 1
            if left<=count<=right:
                temp.append(curr.val)
            curr = curr.next

        count =0
        curr = head
        while curr:
            count += 1
            if left<=count<=right:
                curr.val = temp.pop()
            curr = curr.next

        return head        