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
        courses = defaultdict(list)
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        def dfs(course, visited):
            if course in visited:
                return False
            # Visit the curr vertice, to detect 4 potential cycle
            visited.add(course)
            # dfs through adjacent vertices
            for v in courses[course]:
                if not dfs(v, visited):
                    return False
            # unmark current vertice as visited as we can see it again in another dfs call
            visited.remove(course)
            return True

            
        # 3. try checking the prereqs of every course, if we've encountered a vertice that means there's a cycle
        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True