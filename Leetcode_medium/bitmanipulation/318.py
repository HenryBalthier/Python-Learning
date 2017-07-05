class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n, res = len(words), 0
        word_bits = [0 for i in range(n)]
        # generate a 26 bit mask for every word, each set to 1 if a character is set
        for i in range(n):
            for c in words[i]:
                mask = 1 << (ord(c) - 96)   # Goal!
                word_bits[i] = word_bits[i] | mask
        # for each word, compre to every other word
        for i in range(n):
            for j in range(i + 1, n):
                # if the AND of the two bits are zero, then no overlapping characters
                if word_bits[i] & word_bits[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

s = Solution()
x = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(s.maxProduct(x))
