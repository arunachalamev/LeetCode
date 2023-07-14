class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = collections.defaultdict(int)
        ans = 0
        for a in arr:
            prev_a = d[a-difference]
            d[a] = prev_a + 1
            ans = max(ans, d[a])
        return ans