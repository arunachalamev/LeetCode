# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        #Build a graph from given Tree
        def buildgraph(node,parent):
            if node and parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if node.left:
                buildgraph(node.left,node)
            if node.right:
                buildgraph(node.right,node)
            return

        buildgraph(root,None)
        # print (graph)

        ans = []
        # Perform BFS
        q = deque([(target.val,0)])
        visited = set([target.val])
        while q:
            node,depth = q.popleft()
            if depth == k:
                ans.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei,depth+1))
        return ans