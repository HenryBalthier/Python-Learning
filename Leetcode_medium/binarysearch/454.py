class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        length = len(A)
        a = 0
        A = sorted(A)
        B = sorted(B)
        C = sorted(C)
        D = sorted(D)

        count = 0

        while a < length:
            b = 0
            while b < length:
                c, d = 0, length-1
                while c <= length-1 and d >= 0:
                    tmp = A[a] + B[b] + C[c] + D[d]
                    if tmp < 0:
                        c += 1
                    elif tmp > 0:
                        d -= 1
                    else:
                        print(a, b, c, d)
                        count += 1
                        c += 1
                        d -= 1
                b += 1
            a += 1
        return count



if __name__ == '__main__':
    A = [0, 1, -1]
    B = [-1, 1, 0]
    C = [0, 0, 1]
    D = [-1, 1, 1]
    s = Solution()
    print(s.fourSumCount(A, B, C, D))