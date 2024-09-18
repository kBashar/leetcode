class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([format(num, "b") for num in map(int, date.split("-"))])