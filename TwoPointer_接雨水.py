```
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

与另一道相向指针问题一样， iterate through all heights from left and right towards center, to record the difference of the tallest and the current and add up
```

class Solution:
    def trap(self, height: List[int]) -> int:
      left = 0
      right = len(height)-1
      l_ma = 0 # left tallest height to add
      r_ma = 0  # right tallest height to add
      amount = 0 # to add up from the difference between tallest and current iterate for res

      while left < right:
        
        # keep record the tallest for add amount for the difference between iterator
        r_ma = max(r_ma, height[right])  
        l_ma = max(l_ma, height[left])  

        if r_ma < l_ma:
          amount += r_ma - height[right] # add up difference each col for amount of rain
          right -= 1
        else:
          amount += l_ma - height[left]
          left -= 1

      return amount
      
