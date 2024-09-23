from collections import deque


def edit_distance(word1, word2):
    if word1 == word2:
        return 0
    if len(word1) == 0 or len(word2) == 0:
        return max(len(word1), len(word2))
    i = 0
    j = 0
    w1 = list(word1)
    w2 = list(word2)
    queue = deque((0, 0))
    visited = set()
    num = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            if (i, j) in visited:
                continue
            while i < len(word1) and j < len(word2) and w1[i] == w2[j]:
                i += 1
                j += 1
            if i == len(w1) and j == len(w2):
                return num
            queue.append((i+1, j))
            queue.append((i+1, j+1))
            queue.append((i, j+1))
        num += 1
