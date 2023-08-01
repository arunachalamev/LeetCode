class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [ i for i in range(1,n+1)]

        res = []

        def backtrack(start,state):
            if len(state) == k:
                res.append(state[:])
            
            for i in range(start,n+1):
                state.append(i)
                backtrack(i+1,state)
                state.pop()
            
            return
        backtrack(1,[])
        return res