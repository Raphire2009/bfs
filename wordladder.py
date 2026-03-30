from collections import deque, defaultdict

def ladlength(beginWord: str, endWord: str, wordList:list[str]) -> int:
    
    if endWord not in wordList:
        return 0
    
    L = len(beginWord)
    all_combo = defaultdict(list)

    for word in wordList:
        for i in range(L):
            pattern = word[ :i] + "*" + word[i+1:]
            all_combo[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()

            for i in range(L):
                pattern = word[ :i] + "*" + word[i+1: ]

                for neighbour in all_combo[pattern]:
                    if neighbour == endWord:
                        return level + 1
                        
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, level + 1))

                all_combo[pattern] = []
        return 0
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot" ,"dot" ,"dog" ,"lot" ,"log" ,"cog"]

print(ladlength(beginWord, endWord, wordList))