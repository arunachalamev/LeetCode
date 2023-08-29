class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty, runningsum = 0,0
        ans = 0
        for i,val in enumerate(customers):
            if val == 'Y':
                runningsum -= 1
            else:
                runningsum += 1
            
            if runningsum < min_penalty:
                min_penalty = runningsum
                ans = i + 1
        
        return ans