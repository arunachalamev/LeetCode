class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairweight = []
        for i in range(len(weights)-1):
            pairweight.append(weights[i]+weights[i+1])
        
        pairweight = sorted(pairweight)
        # print (pairweight)
        ans = 0
        for i in range(k-1):
            ans += pairweight[-i-1] - pairweight[i]
        
        return ans