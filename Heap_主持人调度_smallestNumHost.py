'''
有 n 个活动即将举办，每个活动都有开始时间与活动的结束时间，第 i 个活动的开始时间是 starti ,第 i 个活动的结束时间是 endi ,举办某个活动就需要为该活动准备一个活动主持人。

一位活动主持人在同一时间只能参与一个活动。并且活动主持人需要全程参与活动，换句话说，一个主持人参与了第 i 个活动，那么该主持人在 (starti,endi) 这个时间段不能参与其他任何活动。求为了成功举办这 n 个活动，最少需要多少名主持人。

Same as find smallest occupied chair

Use Heap - min binary tree data structure

import heapq

在heap 里， heappush() 会排序将最小的数值排进root， 将end 时间排入heap 里， 在按照以start时间排序好的list 中iterate 找到有end时间（heap）小于start时间的， 表明这个前一个工作可以继续干这个start时间的工作
最后检测heap中的长度 可以得出需要多少host

'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算成功举办活动需要多少名主持人
# @param n int整型 有n个活动
# @param startEnd int整型二维数组 startEnd[i][0]用于表示第i个活动的开始时间，startEnd[i][1]表示第i个活动的结束时间
# @return int整型
#
import heapq
class Solution:
    def minmumNumberOfHost(self , n: int, startEnd: List[List[int]]) -> int:
      host = [] # set the heap for contain sets of the time schedule with unique time schedule

      sort_startEnd = sorted(startEnd, key = lambda x:x[0]) # sort base on the first element of the 2d array

      for i in sort_startEnd:
        if host and i[0] >= host[0]: # i[0]: iterate the start time on sorted startEnd arr, host[0]: earliest end time to compare with start time i[0]
          heapq.heappop(host) # find host that ends early and do the next work
        heapq.heappush(host, i[1]) # push into the End time base on the min-binary tree

      return len(host)
