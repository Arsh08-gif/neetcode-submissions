class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxlen = 0
        occmap = {}
        
        st = 0
        end = 0
        while(st<n and end<n):
            window = end-st+1
            if s[end] in occmap:
                occmap[s[end]] += 1
            else : occmap[s[end]] = 1
            maxocc = max(v for v in occmap.values())
            if window - maxocc > k: 
                occmap[s[st]] -= 1
                st+=1    
            maxlen = max(maxlen,end-st+1)
            end += 1


        return maxlen


# s = "AABABBA", k = 1
# occmap = {a:2,b:2}
# len = 4
    