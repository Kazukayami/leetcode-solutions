class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        validation=0
        n=len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    validation =1
                    indices=[i,j]    
        if validation!=0:
            return indices
        else:
            return -1
            
        

            