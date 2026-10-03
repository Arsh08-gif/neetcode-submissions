class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        x = "".join(c for c in x if c.isalnum())
        n = len(x)
        i = 0
        j = n-1
        while(i<n and j>0 and i<j):
            if x[i] != x[j]: return False
            i+=1
            j-=1
        return True
        