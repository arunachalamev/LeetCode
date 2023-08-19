class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): return False
        
        temp = []
        for ch in str1:
            if ch == 'z':
                temp.append('a')
            else:
                temp.append(chr(ord(ch)+1))
        
        temp = ''.join(temp)
        # print (temp)
        
        i = 0
        for c1,c2 in zip(str1,temp):
            if str2[i] == c1 or str2[i]==c2:
                i += 1
                if i >= len(str2):
                    return True
            
        return i == len(str2)
        