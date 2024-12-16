class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        q = list()
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(q, (dist, (i, j)))

        def find_parent(parent, a):
            if parent[a] != a:
                parent[a] = find_parent(parent, parent[a])
            return parent[a]


        def union_parent(parent, a, b):
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        parent = [
            i for i in range(n)
        ]
        result = 0
        while q:
            dist, (i, j) = heappop(q)
            
            if find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)
                result += dist
        
        return result