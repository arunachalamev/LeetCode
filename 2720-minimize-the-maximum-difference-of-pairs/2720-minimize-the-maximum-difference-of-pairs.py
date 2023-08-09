class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]

        def countValidPairs(threshold):
            count = 0
            index = 0
            while index < len(nums)-1:
                if nums[index+1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        while lo < hi:
            mid = lo + (hi - lo)//2
            if countValidPairs(mid)>= p:
                hi = mid
            else:
                lo = mid +1
        return lo
