"""binart_tree_zigzag_traversal.py

Given the root of a binary tree, return the zigzag level order traversal of its nodes’ values
"""
from collections import deque

class Solution:
    def ZigZagOrder(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result, direction = [], 1
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level[::direction])
            direction *= (-1)
        
        return result
