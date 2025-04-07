class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            p = 1
            r = i + 1
            l = i - 1
            while l >= 0:
                p = p * nums[l]
                l -= 1
            while r < len(nums):
                p = p * nums[r]
                r += 1
            result.append(p)
        return result
    
solution = Solution()
print(solution.productExceptSelf([1,2,4,6]))





# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# This is a two pointer problem where we have a left and a right problem
# We start by iterating through the length of the range of the list
# the we declare l and r as the left andn right pointers
# p is the variable for the product
# we start decreasing the l pointer until its less than zero and r till it increses by the length of the array.