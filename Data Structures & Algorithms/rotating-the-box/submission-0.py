class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # first change the row then rotate

        for row in boxGrid:
            last = len(row) - 1
            stone = len(row) - 1
            while last > 0 and stone > -1:
                # print(last, stone)
                # print(row)
                if row[last] == ".":
                    if row[stone] == "#":
                        row[last] = "#"
                        row[stone] = "."
                        last -= 1
                        stone = last
                    elif row[stone] == "*":
                        last = stone - 1
                        stone = last
                    else:
                        stone -= 1
                else:
                    stone -= 1
                    last -= 1
        ans = []
        for i in range(len(boxGrid[0])):
            # print(ans)
            row = []
            bottom = len(boxGrid) - 1
            while bottom > -1:
                row.append(boxGrid[bottom][i])
                bottom -= 1
            ans.append(row)


        return ans

