class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        entry_map = {}
        max_len = 0
        last_idx = 0
        start = 0
        end = 0
        while(end < len(s)):
            if entry_map and s[end] in entry_map:
                last_idx = entry_map[s[end]]
                if last_idx >= start and last_idx <= end:
                    start = last_idx + 1
            
            entry_map[s[end]] = end
            max_len = max(max_len,end-start+1)
            end += 1
        
        return max_len


                
            