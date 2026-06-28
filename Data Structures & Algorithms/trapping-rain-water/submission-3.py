class Solution:
    def trap(self, height: List[int]) -> int:
    #    0 2 0 3 1 0 1 3 2 1
    #    max = 2 = 3
    #    ans = 2 +2 +3 +2 + 0 
    # two pointer with second pointer checking to see higher point??
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        # Lm = height[0]
        # ans = 0

        # i = 1
        # # Rm = len(height) - 1
        # # while height[Rm -1] > height[Rm]:
        # #     Rm -= 1
        # while i < len(height):
        #     Lm = max(height[i], Lm)
        #     # if Lm > height[i]:
        #     stop = i
        #     while stop < len(height) and height[stop] < Lm:
        #         stop += 1
        #     if stop == len(height):
        #         Lm -= 1
        #     else:
        #         ans += Lm - height[i]
        #         i += 1
        
        # return ans