class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap both see if hashmaps ==
        sMap = {}
        tMap = {}
        for n in s:
            if n not in sMap:
                sMap[n] = 0
            sMap[n] += 1
            
        for x in t:
            if x not in tMap:
                tMap[x] = 0
            tMap[x] += 1
        
        if tMap == sMap:
            return True
        return False
            