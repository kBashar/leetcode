class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = dict()

        for word in strs:
            word_sorted = "".join(sorted(word))
            anagram_list = anagram_map.get(word_sorted)
            if anagram_list:
                anagram_list.append(word)
            else:
                anagram_map[word_sorted] = [word]

        return list(anagram_map.values())


if __name__ == "__main__":
    sol = Solution()

    assert sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
