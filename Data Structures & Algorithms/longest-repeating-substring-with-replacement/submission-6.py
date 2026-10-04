class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        st = 0
        end = 0
        max_len = 0
        while(end < len(s)):
            if freq_map and s[end] in freq_map:
                freq_map[s[end]] += 1
            else : freq_map[s[end]] = 1
            max_freq = max(freq_map.values())
            curr_len = end-st+1
            while (curr_len - max_freq > k):
                freq_map[s[st]] -= 1
                st += 1
                curr_len = end-st+1
                max_freq = max(freq_map.values())
                
            max_len = max(max_len, end-st+1)
            end += 1
        
        return max_len

                


        