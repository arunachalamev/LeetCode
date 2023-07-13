class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for i,j in prerequisites:
            indegree[j] += 1
            graph[i].append(j)
        
        q= deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return True if len(set(ans)) == numCourses else False