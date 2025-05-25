# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            else:
                hashmap[n] = i


# Create an instance of Solution
solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))

# What we do is first get the number and their position in 2 variables using
# enumerate. Then we find out the difference between the first number and 
# the target number because the difference would be the second number we need
# To find the second number we see create a hashmap. For the first time
# since the hasmap is empty we just insert the first number and its position as
# its value. And we interate the loop again. 
# In our case first we insert {3:1} in the hashmap and for second time when the 
# number is 4 the difference is again 3 so we find our two sum.
# Now we return 3's position from the hasmap and 4's position from the currently 
# accessing enumerate values. 