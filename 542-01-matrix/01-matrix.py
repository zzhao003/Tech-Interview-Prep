class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    #     output = [[0] * len(mat[0]) for i in range(len(mat))]
        
    #     for r in range(len(mat)):
    #         for c in range(len(mat[0])):
    #             output[r][c] = self.explore(mat, r, c)

    #     return output

    # def explore(self, mat, r, c):
    #     if mat[r][c] == 0: return 0

    #     position = f'{r},{c}'
    #     visited = set()
    #     visited.add(position)

    #     q = deque([[r, c, 0]])

    #     while(len(q) > 0):
    #         r, c, distance = q.popleft()

    #         if mat[r][c] == 0: return distance

    #         if 0 <= r+1 < len(mat) and 0 <= c < len(mat[0]) and f"{r+1},{c}" not in visited:
    #             q.append([r+1, c, distance + 1])
    #             visited.add(f"{r+1},{c}")
    #         if 0 <= r-1 < len(mat) and 0 <= c < len(mat[0]) and f"{r-1},{c}" not in visited:
    #             q.append([r-1, c, distance + 1])
    #             visited.add(f"{r-1},{c}")
    #         if 0 <= r < len(mat) and 0 <= c+1 < len(mat[0]) and f"{r},{c+1}" not in visited:
    #             q.append([r, c+1 , distance + 1])
    #             visited.add(f"{r},{c+1}")
    #         if 0 <= r < len(mat) and 0 <= c-1 < len(mat[0]) and f"{r},{c-1}" not in visited:
    #             q.append([r, c-1 , distance + 1])
    #             visited.add(f"{r},{c-1}")

    # BFS explore to find the nearest zero is too slow. 
        q = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = '#'
        for k in q:
            r, c = k
            
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nr = r + dx
                nc = c + dy

                if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat

        