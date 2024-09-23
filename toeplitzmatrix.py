from collections import defaultdict


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hashmap = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diff = (j-i)
                hashmap[diff].add(matrix[i][j])

        for diff, val in hashmap.items():
            if len(val) > 1:
                return False
        return True
