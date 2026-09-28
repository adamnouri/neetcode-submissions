class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitsToLetters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        sol = []
        def backtrack(index,subset):
            if index == len(digits):
                sol.append("".join(subset))
                return
            for c in digitsToLetters[digits[index]]:
                backtrack(index+1, subset + c)
                
        


        backtrack(0,"")
        return sol
