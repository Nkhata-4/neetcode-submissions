class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        dist = []
        ans = []
        for coord in points:
            x = coord[0]
            y = coord[1]
            calc = math.hypot(x, y)
            dist.append(calc)
        while k > 0:
            least = dist.index(min(dist))
            ans.append(points[least])
            dist.remove(min(dist))
            points.pop(least)
            k -= 1
        return ans

        
