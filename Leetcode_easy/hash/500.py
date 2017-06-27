class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        lst = []
        for i in words:
            ii = i.lower()
            if set(ii) <= a or set(ii) <= b or set(ii) <= c:
                lst.append(i)
        return lst
if __name__ == '__main__':
    s = Solution
    w = ["Hello", "Alaska", "Dad", "Peace"]
    print(s.findWords(s, w))