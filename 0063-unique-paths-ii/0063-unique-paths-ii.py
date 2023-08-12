class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m==1 and n == 1 and obstacleGrid[0][0]==1:
            return 0

        dp =[[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j==0: 
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i ==0:
                    dp[i][j] = dp[i][j-1]
                    continue
                if j ==0:
                    dp[i][j] = dp[i-1][j]
                    continue
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1] % (2*10**9)