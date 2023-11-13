class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r, c, visited):
                    count += 1
        
        return count

    def explore(self, grid, r, c, visited):
        inBound = r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
        if not inBound: return False

        if grid[r][c] == '0': return False

        position = f"{r},{c}"
        if position in visited: return False

        visited.add(position)

        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c+1, visited)
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r, c-1, visited)

        return True



        