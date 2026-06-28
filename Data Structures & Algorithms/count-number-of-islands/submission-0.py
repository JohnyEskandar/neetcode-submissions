class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            else:
                return
            # if grid[i + 1][j] == "1":
            #     grid[i + 1][j] = "0"
            #     dfs(i + 1, j) 
            # elif grid[i - 1][j] == "1":
            #     grid[i - 1][j] = "0"
            #     dfs(i - 1, j) 
            # elif grid[i][j + 1] == "1":
            #     grid[i][j + 1] = "0"
            #     dfs(i, j + 1) 
            # elif grid[i][j - 1] == "1":
            #     grid[i][j -1] = "0"
            #     dfs(i, j - 1) 
            # else:
            #     return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands