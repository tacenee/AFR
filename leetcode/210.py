class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]
        lesson_map = [set() for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        res = []
        for x, y in prerequisites:
            lesson_map[y].add(x)
            visited[x] += 1
        queue = []
        for i in range(numCourses):
            if visited[i] == 0:
                queue.append(i)
        print(queue)
        while queue:
            lesson = queue.pop(0)
            res.append(lesson)
            for successor in lesson_map[lesson]:
                visited[successor] -= 1
                if visited[successor] == 0:
                    queue.append(successor)
        if len(res) != numCourses:
            return []
        # return res
        print(res)



Solution().findOrder(2,[[1,0]])