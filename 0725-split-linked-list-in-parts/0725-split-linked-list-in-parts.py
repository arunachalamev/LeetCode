# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        count, remainder = n//k, n%k

        ans = []

        curr = head
        
        for i in range(k):
            temp_head = ListNode(0)
            sentinel = temp_head
            target = count + (i<remainder)
            while target > 0:
                sentinel.next = curr if curr else None
                curr = curr.next if curr else None
                sentinel = sentinel.next
                target -= 1
            sentinel.next = None
            ans.append(temp_head.next)

        return ans
