from typing import List
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0
        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left +=1
            ret = max(ret,right-left+1)
            right += 1
        return ret
s = Solution()
nums = [10,1,2,4,7,2]
limit = 5
print(s.longestSubarray(nums,limit))