class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()
        def dfs(crs):
            if crs == []: return True
            if crs in visited: return False
            visited.add(crs)
            for prereq in adjList[crs]:
                if dfs(prereq) == False:
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True
        
        for n in adjList:
            if dfs(n) == False: return False
        return True
