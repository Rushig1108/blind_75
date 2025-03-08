# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                print(hashmap)
            else:
                hashmap[i] = 1
                print(hashmap)
        print(hashmap)
        hashmap = sorted(hashmap, key=lambda x:hashmap[x], reverse=True)[0:k]
        return(hashmap)

solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3], 2))
# We use hashmaps for this problem where we add numbers and thier counts 
# Then we use lambda function to sort the hashmap using values of then keys
# We then sort from 0 to k values of the hasmap