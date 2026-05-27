class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        s = re.sub(r'[^A-Za-z0-9 ]', '', s)
        s = s.lower()
        n = len(s)
        if n==0:
            return True
        i = 0
        while i<=n:
            if (s[i]==s[n-1]):
                i += 1
                n -= 1
            else:
                return False
        return True