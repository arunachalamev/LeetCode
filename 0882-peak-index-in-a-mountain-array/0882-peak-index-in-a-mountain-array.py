class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        lo, hi = 0, len(arr)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1]>arr[mid]>arr[mid+1]:
                hi = mid
            else:
                lo = mid
                
        return lo
        
        