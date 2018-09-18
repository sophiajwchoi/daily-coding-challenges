##Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
##
##
##In Pascal's triangle, each number is the sum of the two numbers directly above it.
##    Example:
##
##    Input: 5
##    Output:
##    [
##         [1],
##        [1,1],
##       [1,2,1],
##      [1,3,3,1],
##     [1,4,6,4,1]
##    ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        li_of_li = []
        for i in range(numRows):
            li = []
            for l in range(i + 1):
                if l == 0 or l == i:
                    li.append(1)
                else:
                    li.append(li_of_li[i - 1][l - 1] + li_of_li[i - 1][l])
            li_of_li.append(li)
        return li_of_li
                    
                    
