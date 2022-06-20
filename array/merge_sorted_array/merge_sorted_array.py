from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        current = m + n - 1
        
        while j > -1:
            if i > -1 and nums1[i] >= nums2[j]:
                nums1[current] = nums1[i]
                i -= 1
            else:
                nums1[current] = nums2[j]
                j -= 1
            
            current -= 1
