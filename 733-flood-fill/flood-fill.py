class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        origianlColor = image[sr][sc]

        self.explore(image, sr, sc, color, visited, origianlColor)

        return image


    def explore(self, image, r, c, color, visited, origianlColor):
        inbound = 0 <= r < len(image) and 0 <= c < len(image[0])
        if not inbound: return 

        if not image[r][c] == origianlColor: return 

        position = f"{r},{c}"
        if position in visited: return 

        visited.add(position)

        if image[r][c] == origianlColor:
            image[r][c] = color

        self.explore(image, r+1, c, color, visited, origianlColor)
        self.explore(image, r-1, c, color, visited, origianlColor)
        self.explore(image, r, c+1, color, visited, origianlColor)
        self.explore(image, r, c-1, color, visited, origianlColor)

        