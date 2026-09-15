class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = [0] * 26
        maxf = 0
        l = 0
        res = 0
        for c in range(len(s)):
            indexR = ord(s[c]) - ord('A')
            indexL = ord(s[l]) - ord('A')
            char[indexR] += 1
            maxf = max(char[indexR], maxf)

            while(c - l + 1 - maxf > k):
                char[ord(s[l]) - ord('A')] -= 1 
                l += 1
            res = max(c-l + 1, res)
        return res
                
