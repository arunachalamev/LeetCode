class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        
        lo, hi = 1, 10**7

        def feasible(speed):
            tot = 0
            for d in dist[:-1]:
                tot += math.ceil(d/speed)
            tot += dist[-1]/speed
            if tot <= hour:
                return True
            else:
                return False


        while lo < hi:
            mid = (lo + hi)//2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
        