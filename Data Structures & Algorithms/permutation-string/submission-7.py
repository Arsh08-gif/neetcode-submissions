class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) : return False
        s1_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i],0) + 1
        
        start = 0
        end = 0
        s2_map = {}
        while(end < len(s1)):
            s2_map[s2[end]] = s2_map.get(s2[end],0) + 1
            end += 1
        
        if s1_map == s2_map: return True

        while(end < len(s2)):
            s2_map[s2[start]] -= 1
            if s2_map[s2[start]] == 0:
                del s2_map[s2[start]]
            start += 1
            s2_map[s2[end]] = s2_map.get(s2[end],0) + 1
            if s1_map == s2_map: return True
            end += 1
        
        return False

            
            


        