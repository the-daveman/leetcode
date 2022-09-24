import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[\W_]+','',s)
        r = s[::-1]
        return True if s == r else False
