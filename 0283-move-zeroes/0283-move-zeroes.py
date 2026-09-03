class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        final=[]
        count = 0 
        for i in nums:
            if i == 0:
                count+=1
            else:
                final.append(i)
        for i in range(count):
            final.append(0)
        nums[:] = final