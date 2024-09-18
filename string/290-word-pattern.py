class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if len(pattern) != len(s_list):
            return False

        letter_map = dict()

        for index, letter in enumerate(pattern):
            word = s_list[index]

            if not letter_map.get(letter) and word not in letter_map.values():
                letter_map[letter] = word

            else:
                mapped_word = letter_map.get(letter)
                if word != mapped_word:
                    return False

        return True