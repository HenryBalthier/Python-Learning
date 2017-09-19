class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        import copy

        weight = len(board)
        lenght = len(board[0])

        def backtracking(board, word, i, j):
            if word == '':
                return True

            li = i - 1 if i > 0 else i
            ri = i + 1 if i < weight - 1 else i
            lj = j - 1 if j > 0 else j
            rj = j + 1 if j < lenght - 1 else j

            for ii in range(li, ri+1):
                for jj in range(lj, rj+1):
                    if board[ii][jj] is None or (ii != i and jj != j):
                        continue
                    #print(board[ii][jj])
                    if board[ii][jj] == word[0]:
                        arr = copy.deepcopy(board)
                        arr[ii][jj] = None
                        #print(arr)
                        f = backtracking(arr, word[1:], ii, jj)
                        if f is True:
                            return True
            return False

        for i in range(weight):
            for j in range(lenght):
                if board[i][j] == word[0]:
                    arr = copy.deepcopy(board)
                    arr[i][j] = None
                    #print(arr)
                    f = backtracking(arr, word[1:], i, j)
                    if f is True:
                        return True

        return False


if __name__ == '__main__':
    s = Solution()
    b = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
    ]
    w = 'ABCB'
    print(s.exist(b, w))