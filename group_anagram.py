# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap  = {}
        for i in strs:
            nstrs = "".join(sorted(i))
            if nstrs in hashmap.keys():
                hashmap[nstrs].append(i)
            else:
                hashmap.update({nstrs: []})
                hashmap[nstrs].append(i)
        return hashmap.values()

solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

# very straight forward solution.
       #access every element-> for loop
        #sort that element -> string.sort()
        #compare the elements 
        #put the same elements in the common lists
    