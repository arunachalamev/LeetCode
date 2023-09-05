"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        d = {}

        temp = head
        while temp:
            copy_node = Node(temp.val)
            d[temp] = copy_node
            temp = temp.next

        temp = head
        sentinel = Node(0)
        clone_head = sentinel

        while temp:
            sentinel.next = d[temp]
            sentinel = sentinel.next
            sentinel.random = d[temp.random] if temp.random else None
            temp = temp.next
        
        sentinel.next = None
        return clone_head.next