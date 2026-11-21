from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_map = defaultdict(list)
        ans = []
        for s in strs:
            key = "".join(sorted(s))
            grp_map[key].append(s)

        for v in grp_map.values():
            ans.append(v)

        return ans      

        