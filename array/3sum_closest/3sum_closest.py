from typing import List

class Solution:
    def ThreeSumClosest(self, nums: List[int], target: int) -> int:        
        diff = float('int')
        nums.sort()
        for i, num in enumerate(nums):
            low = i + 1
            high = len(nums) - 1

            while (low < high):
                sum = num + nums[low] + nums[high]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                
                if sum < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0:
                break
                
        return target - diff
