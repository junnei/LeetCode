class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {i: [] for i in range(numCourses)}
        visited = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            visited[course] += 1
        
        queue = deque([i for i in range(numCourses) if visited[i] == 0])
        order = []
        
        while queue:
            current = queue.popleft()
            order.append(current)
            
            for neighbor in graph[current]:
                visited[neighbor] -= 1
                if visited[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == numCourses:
            return order
        else:
            return list()