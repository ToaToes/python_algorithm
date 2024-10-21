'''
给定一个数组height，长度为n，每个数代表坐标轴中的一个点的高度，height[i]是在第i点的高度，请问，从中选2个高度与x轴组成的容器最多能容纳多少水
1.你不能倾斜容器
2.当n小于2时，视为不能形成容器，请返回0
'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param height int整型一维数组 
# @return int整型
#

class Solution:
    def maxArea(self , height: List[int]) -> int:
      # have left and right, two pointers to move from outside till inside to compare and get largest container
      # check number of element to check if the side is < 2
      l = len(height)
      if l < 2:
        return 0
      
      left = 0
      right = l - 1 # index starts from 0
      ma = 0 # have a max val for container comparison
      
      while left < right: # move till left = right to finish the loop (smallest) (side cant be smaller than 2)
        container = (right - left) * min(height[left], height[right]) # select 2 sides the shortest one to contain
        ma = max(container, ma) # compare and max = the larger container, to get largest

        # iterate short side ahead/back to find bigger side
        if height[left] < height[right]:
          left += 1
        else:
          right -= 1

      return ma
