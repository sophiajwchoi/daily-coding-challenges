##Given a string which consists of lowercase or uppercase letters,
##find the length of the longest palindromes that can be built with those letters.
##
##This is case sensitive, for example "Aa" is not considered a palindrome here.
##

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        length = 0
        for char in s:
            if char not in charMap:
                charMap[char] = 0
            charMap[char] += 1
            if charMap[char] % 2 == 0:
                length += 2
                charMap[char] = 0

        for char in charMap:
            if charMap[char] == 1:
                return length + 1
        return length
