class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(start,arr,visited):
            if start < 0 or start >= len(arr) or start in visited:
                return False
            if arr[start] == 0:
                return True
            visited.add(start)

            return dfs(start+arr[start],arr,visited) or dfs(start-arr[start],arr,visited)


        visited = set()

        if start < len(arr):
            return dfs(start,arr,visited)
        