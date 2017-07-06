class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        leftcorner = grid[0][0]
        unblocked = True
        for i,v in enumerate(grid[0]):
            if v == 1: unblocked = False
            grid[0][i] = 1 * unblocked
        unblocked = leftcorner == 0
        for r in range(1, len(grid)):
            if grid[r][0] == 1: unblocked = False
            grid[r][0] = 1 if unblocked else 0
            for c in range(1, len(grid[0])):
                grid[r][c] = 0 if grid[r][c] == 1 else grid[r-1][c] + grid[r][c-1]
        return grid[-1][-1]

s = Solution()
x = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(s.uniquePathsWithObstacles(x))