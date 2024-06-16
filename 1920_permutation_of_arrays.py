"""
This is based on the permutation of arrays where number inside the array is used as index
"""


class Solution:
    @staticmethod
    def build_array(nums: list[int]) -> list[int]:
        return [nums[num] for num in nums]
