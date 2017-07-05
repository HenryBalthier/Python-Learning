class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def match(word, s):
            ind, L = 0, len(word)
            for ch in s:
                if ch == word[ind]:
                    ind += 1
                    if ind == L:
                        return True
            return False

        d.sort(key=lambda item: (-len(item), item))
        for word in d:
            if match(word, s):
                return word
        return ''

print((9,3)<(6,8))