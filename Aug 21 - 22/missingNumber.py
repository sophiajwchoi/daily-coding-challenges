
##Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
##find the one that is missing from the array.
##Your algorithm should run in linear runtime complexity.
##Could you implement it using only constant extra space complexity?

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for x in nums:
            if x not in num_set:
                num_set.add(x)
        
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
            
