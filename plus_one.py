'''
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
'''


def plusOne(self, digits):
        getdigit = digits[-1] # given the list it will extract the last element and store it in getdigit
        updatedigit = getdigit + 1 # as the increment is by 1 we simply add by 1 assuming all the element is int
        digits[-1] = updatedigit # then simply replacing by indexing to the last element as 122 + 1 gives 123
        
        return digits # finally returning the updated digits

#! the code is not optimized for the case when it is 9 and we need to update the whole set 
# [9] given the input --> new output will be [1,0]  or given the set [2,9,9,9,9] the set will affect the whole set making it [3,0,0,0,0]
# another case will be updating the [2,0,9,8,9] that gives [2,0,9,9,0] affecting only the line ahead of it.
