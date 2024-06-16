"""
This is the code for leetcode problem number 1929 for concatenating the arrays
"""


class Solution:
    @staticmethod
    def get_concatenation(nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums
