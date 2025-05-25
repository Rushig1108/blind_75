# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
#  The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nset = set(nums)
        longest = 0
        for i in nset:
            if (i - 1) not in nset:
                length = 1
                while (i + length) in nset:
                    length += 1
                    longest = max(longest, length)
        return longest
    
solution = Solution()
print(solution.longestConsecutive([2,20,4,10,3,4,5]))