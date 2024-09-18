import string


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        result = " ".join(words[::-1])
        return result