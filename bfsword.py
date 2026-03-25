from collections import deque

def exist_with_path(board, word):
    rows, cols = len(board), len(board[0])
    
    def bfs(start_r, start_c):
        queue = deque()
        # state: row, col, index, visited, path
        queue.append((start_r, start_c, 0, {(start_r, start_c)}, [(start_r, start_c)]))
        
        while queue:
            r, c, i, visited, path = queue.popleft()
            
            # If we've matched the whole word
            if i == len(word) - 1:
                return path  # ✅ return the actual path
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    board[nr][nc] == word[i + 1]):
                    
                    new_visited = visited.copy()
                    new_visited.add((nr, nc))
                    
                    new_path = path + [(nr, nc)]
                    
                    queue.append((nr, nc, i + 1, new_visited, new_path))
        
        return None
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                result = bfs(r, c)
                if result:
                    return result
    
    return None

board = [
    ['C', 'A', 'T', 'F'],
    ['B', 'G', 'E', 'S'],
    ['I', 'T', 'A', 'E'],
    ['S', 'O', 'N', 'G']
]

word = "CAT"

path = exist_with_path(board, word)
print(path)