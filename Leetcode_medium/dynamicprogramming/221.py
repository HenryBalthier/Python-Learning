class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        w = len(matrix)
        if w == 0:
            return 0
        l = len(matrix[0])
        if l == 0:
            return 0
        mm = []
        for i in range(w):
            m = []
            for j in range(l):
                m.append(int(matrix[i][j]))
            mm.append(m)
        matrix = mm[:]
        if w == 1:
            return 1 if sum(matrix[0]) > 0 else 0

        lst = []
        lst.append(matrix[0])
        for i in range(1, w):
            tmp = []
            for j in range(l):
                if j == 0 or matrix[i][j] == 0:
                    tmp.append(matrix[i][j])
                    continue
                if matrix[i-1][j-1] > 0:
                    flag = 0
                    for x in range(1, lst[i-1][j-1] + 1):
                        flag = x
                        if matrix[i][j - x] == 0 or matrix[i - x][j] == 0:
                            flag -= 1
                            break
                    if flag > 0:
                        tmp.append(flag + 1)
                    else:
                        tmp.append(matrix[i][j])
                else:
                    tmp.append(matrix[i][j])
            lst.append(tmp)
        #print(lst)
        Max = []
        for i in lst:
            Max.append(max(i))
        return max(Max) ** 2




if __name__ == '__main__':
    s = Solution()
    x = ["0001","1101","1111","0111","0111"]
    print(s.maximalSquare(x))