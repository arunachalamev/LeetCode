class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        current_count = [0] * k
        n = len(cookies)

        def dfs (i, zero_count):
            # if no distribution possible, return
            if n-i < zero_count:
                return float('inf')
            
            if i == n:
                return max(current_count)

            ans = float('inf')
            for j in range(k):
                # bracktracking template
                if current_count[j] == 0: # assign chocolate
                    zero_count -= 1
                current_count[j] += cookies[i]

                ans = min (ans, dfs(i+1, zero_count))

                # restore the state
                current_count[j] -= cookies[i]
                if current_count[j] == 0:
                    zero_count += 1

            return ans

        return dfs(0,k)