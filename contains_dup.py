'''Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i)>1:
                return True
        return False
