'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Notice!! Prefix means only to compare the first couple chars in the Strings for all 

'''

# First, simply iterate through using double for loop

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 1
        # start from first str, iterate at position 1
        result = ""
        while pos <= len(strs[1]):
            #substring at 1st str
            sub = strs[1][:pos]
            for compare in strs[2:]:
                if sub != compare[:pos]:
                    return result
                result = sub

            pos += 1

        return result


# Second to sort the string alphabetically (by first char) then just have to compare the first and last one to find Common

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    # first sort the List of string alphabetically 
    # with same first char, will be sorted numerically base on num of char inside
    # different, actually would be return ""
    strs = sorted(strs)

    first = strs[0]
    last = strs[-1]
    ans = ""
    
    # to avoid index out of bound
    for pos in range(min(len(first), len(last))):
      if(first[pos] != last[pos]):
        return ans
      ans += first[pos]
      
    return ans
