'''

给定一个长度为n的数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组

输入：[1,2,3,1,2,3,2,2]

返回值：3

说明：最长子数组为[1,2,3] 


Use Stack to append and check if there exists duplicates

'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr: List[int]) -> int:
      stack = []
      count = 0
      iterate = 0
      for i in arr:
        # add element if not already in stack[]
        if i not in stack:
          stack.append(i)
          iterate += 1 # add to the length for compare
        
        # find duplicate, reassign the stack from on step ahead of the INDEX of the duplicate exists in the stack[] 
        elif i not in stack:
          # reassign the stack from 1+ the duplicate index, meaning to remove the duplicate
          # IF THE ELEMENT INDEX AT 0 -> stack[] = [] -> null
          stack = stack[stack.index(i)+1:]
          # after reassign, there is no duplicate anymore, now its okay to add the "pre-duplicate" element in the stack 
          stack.append(i)
          # record the length of the stack now, for compare
          interate = len(stack)

        if count < iterate: # compare to record the longest
          count = iterate

      return count
