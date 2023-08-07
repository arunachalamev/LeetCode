class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) , len(matrix[0])
        lo, hi = 0, m*n - 1
        # print (m,n)
        while lo <= hi:
            mid = ( lo + hi ) //2
            r,c = mid//n, mid % n
            # print (mid, r,c)
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False