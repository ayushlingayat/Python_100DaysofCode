#Brute Force Approach

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            res.append(group)
        return res

# Time Complexity:
# Sorting each pair: O(N^2 * K log K) where K is max length of string
#
# N = number of strings
#
# Space Complexity:
# O(N * K) for storing the result

#Better Approach

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            dic[key].append(word)
        return list(dic.values())

# TC - O(n log n)
# SC - O(n)

#Optimal Approach

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            lst = [0]*26 #to store frequency of char from a to z
            for char in word:
                lst[ord(char)- ord('a')] += 1 #fetching the thing and initializing it 1 if found
            lst = tuple(lst)
            dic[lst].append(word)
        return list(dic.values())

# TC - O(N * K)
# SC - O(N * K)