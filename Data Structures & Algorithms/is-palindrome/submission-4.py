class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c for c in s if c.isalnum())
        cleaned = cleaned.lower()
        f = 0
        l = len(cleaned) -1
        while f < l:
            if cleaned[f] != cleaned[l]:
                return False
            f += 1
            l -= 1

        return True