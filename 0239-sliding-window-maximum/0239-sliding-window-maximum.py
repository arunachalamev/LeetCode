class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        
        result = []
        for i in range(k,len(nums)):
            result.append(nums[q[0]])
            while q and q[0] <= i-k:
                q.popleft()
            
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        result.append(nums[q[0]])

        return result