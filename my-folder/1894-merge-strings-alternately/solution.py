class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0

        result = []
        while len(result) != (len(word1)+len(word2)):
            if i < len(word1):
                char1 = word1[i]
                result.append(char1)
                i+=1
            
            if j < len(word2):
                char2 = word2[j]
                result.append(char2)
                j+=1
        
        return "".join(result)
        
