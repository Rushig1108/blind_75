class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ''
        for i in s:
            if i.isalnum():
                nstr += i.lower()
            else:
                continue
        return nstr == nstr[::-1]
    
solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))