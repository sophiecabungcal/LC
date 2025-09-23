class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curr_alt_gain = 0
        max_alt = 0

        for i in gain:
            curr_alt_gain += i
            max_alt = max(max_alt, curr_alt_gain)

        return max_alt





        
