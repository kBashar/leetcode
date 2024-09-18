class Solution:
    def climbStairs(self, n: int) -> int:
        prev_one, prev_two = 1, 2
        if n == 1:
            return prev_one
        elif n == 2:
            return prev_two
        for i in range(3, n+1):
            temp = prev_one + prev_two
            prev_one = prev_two
            prev_two = temp
        return prev_two
              