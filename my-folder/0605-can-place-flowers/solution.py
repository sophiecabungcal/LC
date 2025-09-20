class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        open_spots = [j for j, plot in enumerate(flowerbed) if plot==0]
        valid_spots = set() #set containing index of valid spots

        # check if every open spot is valid
        for spot in open_spots:
            right_valid = False
            left_valid = False

            if (spot==len(flowerbed)-1) or (spot+1 <= len(flowerbed)-1 and flowerbed[spot+1]==0 and (spot+1 not in valid_spots)):
                right_valid = True
            
            if spot==0 or (spot-1 >= 0 and flowerbed[spot-1]==0 and (spot-1 not in valid_spots)):
                left_valid = True

            if right_valid and left_valid:
                valid_spots.add(spot)
                if len(valid_spots)>=n:
                    return True

        return len(valid_spots)>=n
