class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countA = [0] * 26
        countB = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countA[ord('a') - ord(s[i])] += 1
            countB[ord('a') - ord(t[i])] += 1
        return countA == countB
