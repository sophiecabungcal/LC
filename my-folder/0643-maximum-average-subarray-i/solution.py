class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_sum = max(float('-inf'), window_sum)

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k] # add next num and subtract old
            max_sum = max(max_sum, window_sum)

        return max_sum/float(k)



            

        
