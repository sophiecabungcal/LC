class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 # pointer to iter through list
        j = 0 # pointer to find non-0 elements
        k = len(nums)
        while i < k:
            if nums[i] == 0:
                if (i+1) >= k:
                    return
                    
                j=i+1
                # find nearest non-0 num
                while nums[j] == 0 and j+1<k:
                    j+=1
                
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j=i+1
            else:
                i+=1





        


        
