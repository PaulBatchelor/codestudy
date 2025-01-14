# 2025-01-10 initial attempt: passes initial tests, but TLE
from typing import List
class Solution:
    # initial backtracking attempt
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        squares = []
        sz = len(words[0])

        def backtrack(candidate=[]):
            # validate current candidate
            nrows = len(candidate)
            for i in range(nrows):
                # ensure that col prefix matches row
                row = candidate[i]
                for c in range(nrows):
                    if row[c] != candidate[c][i]:
                        return

            # if you got this far, it's a valid candidate
            # if there are enough candidates, append to results
            if len(candidate) == sz:
                squares.append(candidate.copy())
                return

            # enumerate through next possible candidates
            for word in words:
                candidate.append(word)
                backtrack(candidate)
                candidate.pop()

        backtrack()
        return squares
