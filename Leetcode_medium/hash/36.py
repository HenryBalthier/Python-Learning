class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        if m != 9 or n != 9:
            return False
        s1 = []
        s2 = []
        s3 = []
        # judge n line
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v != '.':
                    s1 += [(v, j)]
                    s2 += [(v, i)]
                    s3 += [(v, i//3, j//3)]
                    print(s1,s2,s3)
        if len(s1) != len(set(s1)) or len(s2) != len(set(s2)) or len(s3) != len(set(s3)):
            return False
        return True

s = Solution()
x = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print(s.isValidSudoku(x))