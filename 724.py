class Solution:
    def runningSum(self, nums):
        sums = []
        sums.append(0)
        for index, n in enumerate(nums[:-1]):
            sums.append(sums[index]+n)
        return sums

    def pivotIndex(self, nums: list) -> int:
        p_index = -1
        l_sum = self.runningSum(nums)
        # sum the array in reversed sequence
        r_sum = self.runningSum(nums[::-1])
        # reverse the result
        r_sum.reverse()

        for index in range(0, len(nums)):
            if l_sum[index] == r_sum[index]:
                p_index = index
                break
        return p_index


if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        [1, 7, 3, 6, 5, 6],  # 0
        [1, 2, 3],  # -1
        [2, 1, -1]
    ]
    # for t_c in test_cases:
    #     print(sol.runningSum(t_c))

    # for t_c in test_cases:
    #     t_c_c = t_c[::-1]
    #     t_c_c = sol.runningSum(t_c_c)
    #     t_c_c.reverse()
    #     print(t_c_c)
    for t_c in test_cases:
        print(sol.pivotIndex(t_c))

"""
[1, 2, 3]
lf -> [0, 1, 3]
rh -> [5, 3, 0]
"""
