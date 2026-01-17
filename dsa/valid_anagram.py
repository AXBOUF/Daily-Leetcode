

class Solution(object):
    def isAnagram(self, s, t):
        est = [] # creating a placeholder for both string
        tse = []
        for i in s:
            est.append(i) #poppulating the list with for loop 
        for y in t:
            tse.append(y) # populatin second lst with for loop
        est.sort() # cheating through built in sort()
        tse.sort() # same story with diff name
        if est == tse: # checking whether the list is same or not if its not return False
            return True
        else:
            return False

### 
### the code doesnot perform best in the time complexity well will try another approach in another commit
