# problem description:
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int):
#         d = {}
#         for i, num in enumerate(nums):
#             if (target-num) in d:
#                 return [d[target-num], i]
#             else:
#                 d[num] = i


# or can have the following:
class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for i, num in enumerate(nums):
            if (target-num) in d:
                return [d[target-num], i]
            else:
                d[num] = i
        return []


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
