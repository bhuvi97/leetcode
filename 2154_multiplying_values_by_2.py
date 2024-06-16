"""
Leetcode problem 2154
"""


class Solution:
    @staticmethod
    def find_final_value(nums: list[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original = original*2
        return original
