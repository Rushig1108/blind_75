
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # this is for storing the count
        freq = [[] for i in range(len(nums) + 1)]
        print(freq) # this is a special array where we store values in the index places according to their occurances
        for n in nums: # this loops check for the occurances and stores the count in the count hashmap
            if n in count.keys():
                count[n] += 1
            else:
                count[n] = 1
        print(count)
        for n, c in count.items(): # this grabs the keys(n which is the value from nums) and their values(c which is n's count) from the hashmap
            freq[c].append(n)
        print (freq) # we update the nested list of position(c) in the frequency list witht he value n
        res = [] # this is the list of the top k value we return
        for i in range(len(freq) - 1, 0, -1): # we iterate through the frequency list
            for num in freq[i]: # we iterate through the nested lists in the frequency list.
                res.append(num) # here num is only the list that contains values(as there can be lists in the frequency list that can be empty)
                if len(res) == k: # when result reaches the limit of the top k freq values we need we stop and return res
                    return res




solution = Solution()
print(solution.topKFrequent([1,2,2,2,3,3,3], 2))

