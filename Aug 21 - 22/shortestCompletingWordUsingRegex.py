import re
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        matching_words = []
        regex = re.compile('[^a-zA-Z]')
        licensePlate = regex.sub('', licensePlate.lower())

        for x in words:
            status = True
            x = regex.sub('', x)
            for y in licensePlate:
                if y not in x or licensePlate.count(y) > x.count(y):
                    status = False
                    break
            if status == True:
                matching_words.append(x)
                
        min_length = 1000
        return_word = ""
        for word in matching_words:
            if len(word) < min_length:
                min_length = len(word)
                return_word = word
        return return_word
