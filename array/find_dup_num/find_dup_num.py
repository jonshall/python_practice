"""find_dup_num.py

Find and return the duplicate number
"""
class Solution:
    def FindDuplicate(self, nums):
        # Find the intersection point of the two runners
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
