class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort() # sort by start time
        n = len(events)
        
        #DP store the states - dimension (k+1) x n
        dp = [[-1]*n for _ in range(k+1)]
        
        #Store the start time for binary search
        start = [ e[0] for e in events] 
        
        
        def dfs(current_index, count):
            # return condition
            if current_index == n or count == 0:
                return 0
            # return if value calcuated
            if dp[count][current_index] != -1:
                return dp[count][current_index]
            # Fetch the **next index** after the end time 
            next_index = bisect_right(start, events[current_index][1])
            
            #Either to select or dont select and then get the max
            dp[count][current_index] = max(dfs(current_index+1,count) , events[current_index][2] + dfs(next_index, count -1))
            
            return dp[count][current_index]
        

        return dfs(0,k)
            
        