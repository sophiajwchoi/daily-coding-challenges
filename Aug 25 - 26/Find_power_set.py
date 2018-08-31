##Given a set of distinct integers, nums, return all possible subsets (the power set).
##
##Note: The solution set must not contain duplicate subsets.
##
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        for i in range(2 ** len(nums)):
            subset = []
            for k in range(len(nums)):
                if i & 1 << k:
                    subset.append(nums[k])
            subsets.append(subset)
        return subsets


##Another approach 
    def powerset(li):
        result = [[]]
        for x in li:
            new_subset = [subset + [x] for subset in result]
            result.extend(new_subset)
        return result
