class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        freq_count_s1 = {}
        for i in range(len(s1)):
            freq_count_s1[s1[i]] = freq_count_s1.get(s1[i],0)+1

        freq_count_s2 = {}
        st = 0
        end = 0
        while(end < len(s1)):
            freq_count_s2[s2[end]] = freq_count_s2.get(s2[end],0)+1
            if freq_count_s2 == freq_count_s1: return True
            end += 1
        
        
        for j in range(end,len(s2)):
            freq_count_s2[s2[j]] = freq_count_s2.get(s2[j],0)+1
            freq_count_s2[s2[st]] -= 1
            if freq_count_s2[s2[st]] == 0: del freq_count_s2[s2[st]]
            st += 1
            if freq_count_s2 == freq_count_s1: return True

        return False


            

        