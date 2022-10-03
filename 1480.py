class Solution:
    def runningSum(self, nums):
        sums = []
        for index, n in enumerate(nums):
            if index == 0:
                sums.append(n)
            else:
                sums.append(sums[index-1]+n)
        return sums

# class Solution:
#     def runningSum(self, nums):
#         sums = []
#         sums.append(nums[0])
#         for index, n in enumerate(nums[1:]):
#             sums.append(sums[index]+n)
#         return sums

# class Solution:
#     def runningSum(self, nums):
#         sums = []
#         seed = 0
#         for index, n in enumerate(nums):
#             sums.append(seed+n)
#             seed = sums[index]
#         return sums


if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1, -1, 5, 1, 9, 10, 1]))
