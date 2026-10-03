class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m < n: return False
        
        s1_freq = {}
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1

        s2_freq = {}
        for c in s2[:n]:
            s2_freq[c] = s2_freq.get(c, 0) + 1

        if s2_freq == s1_freq:
            return True

        last_char = 0
        for k in range(n,m):
            if s2[k] in s2_freq:
                s2_freq[s2[k]] += 1
            else : s2_freq[s2[k]] = 1
            s2_freq[s2[last_char]] -= 1
            if s2_freq[s2[last_char]] == 0: del s2_freq[s2[last_char]]
            last_char += 1
            if s2_freq == s1_freq : return True
        

        return False
                
                    
# s1="adc"
# s2="dcda"
