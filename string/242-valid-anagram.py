class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same length
        # same set of charecters
        # count of each characters should be same
        
        if len(s) != len(t):
            return False

        letter_map = dict()

        for ch in s:
            if not letter_map.get(ch):
                letter_map[ch] = 1
            else:
                letter_map[ch] += 1

        for ch in t:
            if letter_map.get(ch) and letter_map.get(ch) > 0:
                letter_map[ch] -= 1
            else:
                return False

        return True
  