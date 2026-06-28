class Solution:
    def myPow(self, x: float, n: int) -> float:

        power = abs(n)
        ans = x
        for _ in range(power -1):
            ans *= x
        print(ans)
        if n == 0:
            return 1
        elif n > 0:
            return ans
        else:
            return 1/ans