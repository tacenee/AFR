class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if len(prerequisites) == 0: return True
        # 记录它之前有多少门课程
        in_degreed = [0 for _ in range(numCourses)]
        # 记录每门先学的课程，他可学到哪些课程
        set_map = [set() for _ in range(numCourses)]

        for x, y in prerequisites:
            in_degreed[x] += 1
            set_map[y].add(x)
        queue = []
        for i in range(numCourses):
            # 如果学这门课程前，不需要学其他的课程，就把它加到起始队列
            if in_degreed[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.pop()
            count += 1
            for num in set_map[node]:
                in_degreed[num] -= 1
                # 如果他之前的课程都学完了，它的入度为0.
                if in_degreed[num] == 0:
                    queue.append(num)

        return count == numCourses
