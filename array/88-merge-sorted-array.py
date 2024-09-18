from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_pointer = m - 1
        nums2_pointer = n - 1

        for index in range(m + n - 1, -1, -1):
            if nums2_pointer == -1:
                nums1[index] = nums1[nums1_pointer]
                nums1_pointer -= 1
            elif nums1_pointer == -1:
                nums1[index] = nums2[nums2_pointer]
                nums2_pointer -= 1
            elif nums2[nums2_pointer] == nums1[nums1_pointer]:
                nums1[index] = nums2[nums2_pointer]
                nums2_pointer -= 1
            elif nums2[nums2_pointer] > nums1[nums1_pointer]:
                nums1[index] = nums2[nums2_pointer]
                nums2_pointer -= 1
            else:
                nums1[index] = nums1[nums1_pointer]
                nums1_pointer -= 1