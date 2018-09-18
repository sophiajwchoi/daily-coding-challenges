class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temp, i))
        return res
