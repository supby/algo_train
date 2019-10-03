'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)        
        diff_map = {}
        for i in range(len_nums):
            diff_map[target - nums[i]] = i
        
        ret = []
        for i in range(len_nums):
            diff_i = diff_map.get(nums[i], None)
            if diff_i and i != diff_i and nums[diff_i] + nums[i] == target:
                return [i, diff_i]