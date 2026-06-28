class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find a 1 then ans += 1 then turn all the surrounding 1s to 0s

        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        
        def dfs(i, j):
            if (i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans