class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # problem is: find cycle in a directed acyclic graph
        # Build adjacency list graph with the prereqs, and then dfs through it ex. 0 -> [1, 2, 3] meaning to take course 0 you must take course 1, 2, and 3
        # how 2 detect cycle? 0 -> [1] 1 -> [0]
        # make a visited set, if we've already encountered course 0 then that means it's a cyc
        # for course in range(numCourses): visit each course's prereqs and add the current course to visited set and then visit those nodes
        # numCourses = 5, prerequisites = [[0,1], [1, 2], [2, 3], [2, 4], [3, 1]]
        # 0 : [1]
        # 1 : [2]
        # 2 : [3, 4]
        # 3 : [0]
        # 1. build adj list
        courses = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)
        print(courses)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            # iterate through list
            for v in courses[course]:
                if not dfs(v):
                    return False
            visited.remove(course)
            return True

            
        # 3. try checking the prereqs of every course, if we've encountered a vertice that means there's a cycle
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True