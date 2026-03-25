graph = {
    'I': ['J', 'K'],
    'J': ['I', 'L', 'M'],
    'K': ['I', 'N'],
    'L': ['J'],
    'M': ['J'],
    'N': ['K'],
}

from collections import deque

def bfs_path(graph, start, target):
    queue = deque([(start, [start])])  # (current_node, path)
    visited = set()

    while queue:
        current, path = queue.popleft()

        print("Checking:", current)

        if current == target:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                queue.append((neighbor, path + [neighbor]))

    return None

result = bfs_path(graph, 'I', 'N')
print("Path:", result)