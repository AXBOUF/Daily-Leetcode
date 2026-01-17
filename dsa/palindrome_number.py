#palindrome number 
# given input 12321 == 12321 return True 
# if given input 12344 != 44321
#thought process
# break apart the number, reverse it,if equals to initial nunmber return True 
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]: #it traverse the str from back 
            return True
        else:
            return False
