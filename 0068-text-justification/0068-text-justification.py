class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res,curr,noOfLetters = [],[],0

        for w in words:
            if noOfLetters + len(w) + len(curr) > maxWidth:
                for i in range(maxWidth-noOfLetters):
                    curr[i%(len(curr)-1 or 1)] += ' '
                res.append(''.join(curr))
                curr, noOfLetters = [],0

            curr += [w]
            noOfLetters += len(w)
        
        return res+[' '.join(curr).ljust(maxWidth)]