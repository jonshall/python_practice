"""snakes_and_ladders.py

Simulate chutes and ladders game
"""
import collections
from typing import List

class Solution:
    def SnakesAndLadders(self, board: List[List[int]]) -> int:
        num = len(board)
        def label_to_position(label):
            row, col = divmod(label - 1, num)
            if row % 2 == 0:
                return num - 1 - row, col
            else:
                return num - 1 - row, num - 1 - col
            
        seen = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            row, col = label_to_position(label)
            if board[row][col] != -1:
                label = board[row][col]
            if label == num * num:
                return step
            for i in range(1, 7):
                new_label = label + i
                if new_label <= num * num and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step + 1))
        return -1
