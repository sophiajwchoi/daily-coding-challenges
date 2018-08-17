class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = len(prerequisites)
        if n == 0 or numCourses == 0:
            return True
        g = collections.defaultdict(list)
        
        for curr,pre in :
            g[pre].append(curr)
        visited = set()
        stack = set()

        def dfs(visited, stack, v):
            visited.add(v)
            stack.add(v)
            for nei in g[v]:
                if nei not in visited:
                    if dfs(visited, stack, nei):
                        return True
                else:
                    if nei in stack:
                        return True
            stack.discard(v)
            return False

        for i, j in prerequisites:
            if j not in visited:
                if dfs(visited, stack, j):
                    return False
        return len(visited) <= numCourses
