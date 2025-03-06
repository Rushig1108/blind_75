# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {} #this stores the values as dict
        for i in strs:
            sort = ''.join(sorted(i)) #sort the word
            if sort in anagram.keys(): # if the key is present  
                anagram[sort].append(i) # put the unsorted element to that key
            else: #if not
                anagram.update({sort:[]}) #insert the key
                anagram[sort].append(i) # put the unsorted element to the key
        return anagram.values() # return just the values
    
solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

# very straight forward solution.
       #access every element-> for loop
        #sort that element -> string.sort()
        #compare the elements 
        #put the same elements in the common lists