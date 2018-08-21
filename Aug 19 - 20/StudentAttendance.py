##You are given a string representing an attendance record for a student.
##The record only contains the following three characters:
##'A' : Absent.
##'L' : Late.
##'P' : Present.
## A student could be rewarded if his attendance record doesn't
## contain more than one 'A' (absent) or more than two continuous 'L' (late).
##
##You need to return whether the student could be rewarded according to
##his attendance record.

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        count = 0
        for x in s:
            if x == "L":
                stack.append(x)
            if x == "A":
                count += 1
            if x != "L":
                stack = []
            if len(stack) >= 3 or count >= 2:
                return False
        return True
