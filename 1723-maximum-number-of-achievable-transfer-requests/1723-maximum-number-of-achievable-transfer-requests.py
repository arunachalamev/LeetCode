class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # Search which max k will satisfy the condition
        for k in range(len(requests),0,-1):
            # get 'k' combination of request from given lenght of request
            for c in itertools.combinations(range(len(requests)),k):
                deg = [0]* n
                # from the given combinations add and sub degree
                for i in c:
                    deg[requests[i][0]] -= 1
                    deg[requests[i][1]] += 1
                if not any(deg):
                    return k
        return 0

# Time Complexity: O(len(request) * 2^len(request))
