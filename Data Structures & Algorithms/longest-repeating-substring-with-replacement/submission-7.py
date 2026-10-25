class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq_map = {}
        start = 0
        end = 0
        max_length = 0
        while(end < n):
            freq_map[s[end]] = freq_map.get(s[end],0)+1
    
            while (end-start+1) - max(freq_map.values()) > k :
                freq_map[s[start]] -= 1
                start += 1
                
            max_length = max(max_length, end-start+1)
            end += 1
        
        return max_length
                



        