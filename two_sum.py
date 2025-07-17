#given an array of integers 
#an a target 
#return indices of the two numbers such that 
#they add up to target 


#[2,7,11,15] ~ 9 output is [0,1]
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            cn = i 
            for j in range(i+1,len(nums)):
                if nums[cn] + nums[j] == target:
                    return ([cn,j])


'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
