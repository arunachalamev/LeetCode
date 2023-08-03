class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}


        def helper(digits):
            if len(digits) == 1:
                return list(d[digits])
            if len(digits) <= 0:
                return []
            
            res = []
            temp = helper(digits[1:])
            for x in temp:
                for ch in d[digits[0]]:
                    res.append(''.join(ch+x))
            return res

    
        ans =  helper(digits)

        return ans