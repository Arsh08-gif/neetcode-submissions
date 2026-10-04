class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) : return ""
        freq_map_t = {}
        for i in range(len(t)):
            freq_map_t[t[i]] = freq_map_t.get(t[i],0) + 1
        
        freq_map_s = {}
        st = 0
        end = 0
        min_len = float('inf')
        ans = ""
        required = len(freq_map_t)
        formed = 0
        while(end < len(s)):
            if s[end] in freq_map_t:
                freq_map_s[s[end]] = freq_map_s.get(s[end],0) + 1
                if freq_map_s[s[end]] == freq_map_t[s[end]]:formed += 1
            while formed == required:
                if min_len > end-st+1:
                    min_len = end-st+1
                    ans = s[st:end+1]
                if s[st] in freq_map_s: 
                    if freq_map_s[s[st]] == freq_map_t[s[st]]: formed -= 1
                    freq_map_s[s[st]] -= 1
                    if freq_map_s[s[st]] == 0: del freq_map_s[s[st]]
                st += 1
            end += 1
        
        return ans




        