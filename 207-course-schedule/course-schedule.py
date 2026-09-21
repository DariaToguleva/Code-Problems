class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = set()
        work = set()

        d = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] in d:
                d[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                d[prerequisites[i][0]] = [prerequisites[i][1]]      
        def dfs(x):
            if x in visited:
                return True
            if x in work:
                return False

            work.add(x)
            for val in d.get(x, []):
                if not dfs(val):
                    return False
            work.remove(x)
            visited.add(x)   
            return True     
        return all(dfs(i) for i in range(numCourses))        