class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)

        for course, pre in prerequisites:
            courses[course].append(pre)
        
        # numCourses = 5, prerequisites = [[0,1], [1, 2], [2, 3], [2, 4]]
        # 0 : [1]
        # 1 : [2]
        # 2 : [3, 4]
        # 3 : []
        # 4 : []
        # res = [3, 4, 2, 1, 0]
        res = []
        visited = set()
        completed = set()
        def dfs(course):
            # found a cycle
            if course in visited:
                return False
            # we've already finished processing this node, no need to add it again
            if course in completed:
                return True

            visited.add(course)
            for v in courses[course]:
                if not dfs(v):
                    return False
            visited.remove(course)
            # Done with this course
            completed.add(course)
            res.append(course)
            return True
            
        for i in range(numCourses):
            # cycle found
            if not dfs(i):
                return []

        return res


            
        