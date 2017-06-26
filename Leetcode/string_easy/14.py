class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        s = strs[0]
        n = 99999
        for i in strs:
            l = len(i)
            if l < n:
                n = l
            while s[:n] != i[:n]:
                n -= 1
            print(s[:n])
            s = i[:n]
        return s

if __name__ == '__main__':
    s = Solution()
    x = ['aaabc', 'aaasdd', 'aa', 'aacddqwdesad']
    print(s.longestCommonPrefix(x))