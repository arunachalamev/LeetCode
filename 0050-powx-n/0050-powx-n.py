class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 0
        if n <0 :
            flag = 1
        
        x,n = x, abs(n)
        
        def calculate(x, n):
            if n <=0:
                return 1
            half = calculate(x,n//2)
            if n& 1 == 1:
                return half * half * x
            else:
                return half * half
        
        return 1/calculate(x,n) if flag else calculate(x,n)
        