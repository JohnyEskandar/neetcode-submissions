class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        minLength = float("inf")
        left = 0
        tVals = defaultdict(int)
        for char in t:
            tVals[char] += 1
        
        for right in range(len(s)):
            if s[right] in tVals:
                tVals[s[right]] -= 1
            while max(tVals.values()) == 0:
                if right-left < minLength:
                    minLength = right-left
                    ans = s[left:right+1]
                if s[left] in tVals:
                    tVals[s[left]] += 1
                left += 1
        
        return ans