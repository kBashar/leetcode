class Solution:
    def canConstruct(self, ransomeNote: str, magazine: str) -> bool:
        if len(ransomeNote) > len(magazine):
            return False

        magazine_map = [0] * 26

        for letter in magazine:
            letter_index = ord(letter) - 97
            magazine_map[letter_index] += 1

        for letter in ransomeNote:
            letter_index = ord(letter) - 97
            magazine_map[letter_index] -= 1
            if (magazine_map[letter_index]) < 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.canConstruct("a", "b") == False
    assert sol.canConstruct("a", "ba") == True
    assert sol.canConstruct("aaa", "aaaab") == True
    assert sol.canConstruct("aa", "ab") == False
