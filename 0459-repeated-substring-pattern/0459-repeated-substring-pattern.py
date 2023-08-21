class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)
        i = 1
        while i<= n//2:
            if n%i == 0:
                noOfReplication = n//i
                if s[:i]*noOfReplication == s:
                    return True
            i += 1

        return False