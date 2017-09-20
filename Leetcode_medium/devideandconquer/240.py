class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]]:
            return False

        for lst in matrix:
            if lst == []:
                break
            if lst[-1] < target:
                continue
            if lst[0] > target:
                break
            if target in lst:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    x = [
[]
]
    t = 20
    print(s.searchMatrix(x, t))