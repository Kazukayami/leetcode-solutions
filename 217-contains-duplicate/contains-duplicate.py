class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        for i,value in enumerate(nums):
            if value in dict:
                return True
            dict[value]=i
        return False