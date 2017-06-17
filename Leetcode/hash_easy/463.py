class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = len(grid[0])
        grid = [[ 0 ] * l] + grid + [[ 0 ] * l]
        for i, v in enumerate(grid):
            grid[i] = [0] + v + [0]
        sum = 0
        count = 0
        for i, v in enumerate(grid):
            for j, w in enumerate(grid[i]):
                if grid[i][j] == 1:
                    sum += grid[i][j+1] + grid[i+1][j] + grid[i][j-1] + grid[i-1][j]
                    count += 4
        return count - sum



if __name__ == '__main__':
    s = Solution
    g = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
    print(s.islandPerimeter(s, g))