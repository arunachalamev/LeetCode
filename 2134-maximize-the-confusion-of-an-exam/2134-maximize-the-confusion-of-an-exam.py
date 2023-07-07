class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = k
        count = collections.Counter(answerKey[:k])
        left = 0
        for right in range(k,len(answerKey)):
            count[answerKey[right]] += 1

            while min(count['T'], count['F']) > k:
                count[answerKey[left]] -= 1
                left += 1
            
            ans = max(ans, right-left + 1)
        
        return ans