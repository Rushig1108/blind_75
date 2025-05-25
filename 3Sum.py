class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            l, r = i +1, len(nums) -1
            while l < r:
                threesum = n + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    result.append([n ,nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
        return result

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))        