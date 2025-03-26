from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        print("Encoded:", res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # Extract full number before #
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        print("Decoded:", res)
        return res

# Create an instance
sol = Solution()

# Sample test case
test_input = ["we", "say", ":", "yes", "!@#$%^&*()"]

# Encoding
encoded_str = sol.encode(test_input)

# Decoding
decoded_list = sol.decode(encoded_str)

# Verifying if decode(encode(test_input)) returns the original list
assert decoded_list == test_input, "Test failed!"
print("Test passed successfully!")


#Explanation:
## For encoding 
        # iterating through the list 
        # putting length of the word and a "#" in front of every word
        # the length helps us interate while decoding and # makes sure that
        # if the word contains a number those are excluded.
        #return one single string 
## For Decoding
        # interating through the string
        # using a expanding windows to check for the length of the string and #
        # using i to interate and j to find the "#"
        # initializing i on zero position first 
        # starting to interate i until it exceeds the length of the string
            # stating j with the value of i
            # starting a while loop until j is "#"
            # as soon as we find # we know that the character before the existing j is the length of the words
            # getting the length using the value of i 
            # changing the value of i to i + j 
            # shifting j to one character after the last character of the word 
            # grabbing the word from i to j 
            # storing it in a list 
            # shifting the value of i to j i.e i = j
            # breaking the first while loop
        # returning the list of words
