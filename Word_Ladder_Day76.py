from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # For O(1) lookups
        if endWord not in wordSet:
            return 0

        # Preprocessing: Create adjacency patterns
        adj = defaultdict(list)
        wordLen = len(beginWord)

        for word in wordSet:
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        # BFS
        queue = deque([(beginWord, 1)])  # (word, steps)
        visited = set([beginWord])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in adj[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))
        return 0

# Time Complexity:
# Preprocessing adjacency: O(N * L) where
# N = number of words in wordList,
# L = length of each word.
# BFS traversal: O(N * L) (each transformation checked once).
# Total → O(N * L)

# Space Complexity:
# Adjacency dictionary: O(N * L)
# Queue + visited set: O(N)
# Total → O(N * L)

