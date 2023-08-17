class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])

        queue = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = -1
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            r,c = queue.popleft()

            for x,y in direction:
                new_r, new_c = r+x, c+y
                if 0<=new_r<m and 0<=new_c<n and mat[new_r][new_c] == -1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r,new_c))
        
        return mat