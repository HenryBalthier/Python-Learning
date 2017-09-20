class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lst = []
        for i in matrix:
            lst += i
        lst = sorted(lst)
        return lst[k-1]

if __name__ == '__main__':
    s = Solution()
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8
    print(s.kthSmallest(matrix, k))