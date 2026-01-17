class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for y in range(i+1,len(nums)):
                if nums[i] == nums[y]:
                    return True
        return False 

#this is a brute force approach but it doesnot passes all the test cases 

# time limit exceeded 
        
