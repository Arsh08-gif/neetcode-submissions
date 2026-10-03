class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        # for i in range(n):
        #     seen = []
        #     for j in range(i,n):
        #         if seen and s[j] in seen: break
        #         substr = s[i:j+1]
        #         seen.append(s[j])
        #         maxlen = max(maxlen, j-i+1)

        seen = {}
        st = 0
        end = 0
        maxlen = 0
        while(st < n and end < n):
            if seen and s[end] in seen:
                stidx = seen[s[end]]
                if stidx <= end and stidx >= st:
                    st = stidx + 1
            
            seen[s[end]] = end
            maxlen = max(maxlen, end-st+1)
            end += 1
                
        
        return maxlen


# s = "abbaacdef"
# len = 5
# seen = [a:4,b:2,c:5,d:6,e:7,f:8]
# indx <= end
# st += seen[z] + 1
