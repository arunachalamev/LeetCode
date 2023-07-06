class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot = 0
        l = 0
        ans = float('inf')
        for r in range(len(nums)):
            tot += nums[r]

            while tot >= target:
                ans = min(ans, r-l+1)
                tot -= nums[l]
                l += 1
            
        if ans != float('inf'):
            return ans
        else:
            return 0            