class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        [1, 0]  # 0
        [1, 2, 3] # -1
    ]
    for t_c in test_cases:
        print(sol.pivotIndex(t_c))
