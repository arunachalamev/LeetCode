class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        index = [-1]
        for i,v in enumerate(nums):
            if v == 0:
                index.append(i)
        
        index.append(len(nums))
        ans = 0
        if len(index) <= 2:
            return len(nums)-1
        else:
            for i in range(1,len(index)-1):
                ans = max(ans, index[i+1] - index[i-1] - 2)
        return ans