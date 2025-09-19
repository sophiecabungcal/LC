class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1

        s_list = list(s)

        vowels = set("aeiouAEIOU")

        # stop condition: if i+1 = j or j-1 = i

        while i < j:
            while i < j and s_list[i] not in vowels:
                i+=1
            
            while j > i and s_list[j] not in vowels:
                j-=1

            s_list[i], s_list[j] = s_list[j], s_list[i]
            i+=1
            j-=1

        return "".join(s_list)
