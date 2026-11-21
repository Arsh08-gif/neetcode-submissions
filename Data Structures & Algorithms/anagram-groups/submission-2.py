from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_map = defaultdict(list)
        ans = []
        # for s in strs:
        #     key = "".join(sorted(s))
        #     grp_map[key].append(s)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1
            grp_map[tuple(count)].append(s)

        # for v in list(grp_map.values()):
        #     ans.append(v)

        # return ans  
        return list(grp_map.values())    

        