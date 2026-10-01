class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
    
        if len(s1) > len(s2):
            return False
        s2Window = [0] * 26
        for i in range(len(s1)):
            s2Window[ord(s2[i]) - ord('a')] += 1
            s1Count[ord(s1[i]) - ord('a')] += 1
        if s2Window == s1Count:
                return True    
        for i in range(len(s1), len(s2)):
            s2Window[ord(s2[i - len(s1)])- ord('a')] -= 1
            s2Window[ord(s2[i])- ord('a')] += 1
            if s2Window == s1Count:
                return True   
        return False

            