class Solution:

    def encode(self, strs: List[str]) -> str:
        # code = "".join(f"{len(s)}#{s}" for s in strs)
        for i,s in enumerate(strs):
            strs[i] = str(len(s))+ "#" + s
        
        code = "".join(strs)
        return code
    def decode(self, s: str) -> List[str]:
        m = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            m.append(s[j+1:j+l+1])
            i = l + j +1
        return m