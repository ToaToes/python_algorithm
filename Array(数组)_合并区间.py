'''
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。


输入：
[[10,30],[20,60],[80,100],[150,180]]

返回值：
[[10,60],[80,100],[150,180]]

use list to compare
'''

# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#

class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:

      intervals = sorted(interval, key = lambda x: x.start)

      res = [intervals[0]] # get the first from the sorted list, for compare later

      # iterate the interval list and compare
      # next.start > res[-1].end -> cant merge, append to the list, as the new [-1] to compare with the next iterate
      # else next.end > res[-1].end -> reassign end

      for i in interval[-1]:
        if i.start > res[-1].end:
          res.append(intervals[i])
        elif i.end > res[-1].end: # contains 2 condition: 1. i.end > res[-1].end, i.start < res[-1].end(already compared).   if i.end < res[-1].end, no need for reassign
          res.end = i.end

      return res
