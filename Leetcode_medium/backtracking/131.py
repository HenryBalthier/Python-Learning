class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def func(s, idx, cur):
            if idx >= length:
                res.append(cur[::])

            for i in range(idx, length):
                tmp = s[idx: i+1]
                cur.append(tmp)
                if tmp == tmp[::-1]:
                    func(s, i+1, cur)
                cur.pop()

        res = [[]]
        length = len(s)
        func(s, 0, [])
        return res




if __name__ == '__main__':
    s = Solution()
    x = 'aab'
    print(s.partition(x))