class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        N = max(len(v1), len(v2))
        for i in range(N):
            m_1 = v1[i] if i < len(v1) else 0
            m_2 = v2[i] if i < len(v2) else 0
            if m_1 > m_2:
                return 1
            elif m_1 < m_2:
                return -1
        return 0



s = Solution()
x = '1.23'
y = '1.3'
print(s.compareVersion(x, y))