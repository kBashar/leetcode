class Solution:
    def __init__(self):
        self.vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    def romanToInt(self, s: str) -> int:
        sum = 0
        previous_val = 0
        for c in s[::-1]:
            present_val = self.vals[c]
            if present_val < previous_val:
                sum -= present_val
            else:
                sum += present_val
            previous_val = present_val
        print(sum)
        return sum

if __name__=="__main__":
    sol = Solution()
    sol.romanToInt('MCMXCIV')
    sol.romanToInt('IV')
    sol.romanToInt('MC')
    sol.romanToInt('CM')