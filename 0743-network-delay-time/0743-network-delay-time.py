class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        MAX_INT = sys.maxsize
        graphs = [
            list()
            for _ in range(n+1)
        ]

        for u, v, w in times:
            graphs[u].append((v, w))

        distance = [
            MAX_INT for _ in range(n+1)
        ]
        distance[k] = 0

        q = list()
        heapq.heappush(q, (0, k))

        while q:
            dist, x = heapq.heappop(q)
            if distance[x] < dist:
                continue

            for nx, cost in graphs[x]:
                if dist + cost < distance[nx]:
                    distance[nx] = dist + cost
                    heappush(q, (dist + cost, nx))
        
        if MAX_INT in distance[1:]:
            return -1
        else:
            return max(distance[1:])