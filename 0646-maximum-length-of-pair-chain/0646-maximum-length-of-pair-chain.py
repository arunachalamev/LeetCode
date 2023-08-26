class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key= lambda e: e[1])
        end = pairs[0][1]
        count = 1
        for i in range(1,len(pairs)):
            if end < pairs[i][0]:
                count += 1
                end = pairs[i][1]
            
        return count