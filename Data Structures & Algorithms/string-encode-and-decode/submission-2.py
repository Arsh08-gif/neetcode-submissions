class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += st
            s += "ñ"
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        st_list = s.split("ñ")
        return st_list[:-1]
