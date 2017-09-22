class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        w = len(matrix)
        if w == 0:
            return
        l = len(matrix[0])
        if l == 0:
            return
        lst = []
        tmp = [matrix[0][0]]
        for i in range(1, l):
            tmp.append(tmp[i-1] + matrix[0][i])
        lst.append(tmp)
        for i in range(1, w):
            tmp = [matrix[i][0] + lst[i-1][0]]
            for j in range(1, l):
                tmp.append(matrix[i][j] + lst[i-1][j] + tmp[j-1] - lst[i-1][j-1])
            lst.append(tmp)
            print(lst)
        self.lst = lst

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        lst = self.lst
        res = lst[row2][col2]
        if row1 > 0:
            res -= lst[row1 - 1][col2]
        if col1 > 0:
            res -= lst[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += lst[row1 - 1][col1 - 1]
        return res

if __name__ == '__main__':
    m = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
    s = NumMatrix(m)
    print(s.sumRegion(2, 1, 4, 3))
