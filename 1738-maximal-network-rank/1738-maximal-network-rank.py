class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        maxRank = 0
        for i in range(n):
            for j in range(i+1, n):
                tot = len(graph[i]) + len(graph[j])

                if j in graph[i]:
                    tot -= 1
                
                maxRank = max(maxRank,tot)
        
        return maxRank