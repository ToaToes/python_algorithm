'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

So 1-step and 2-step are only two ways to climb, so unique for both
Then has to consider how many steps to reach, before taking either 1-step or 2-step

So: Steps(n) = Step(n-1) + Step(n-2)

Step(n-1): how many ways to reach the stage that only needs one step
Step(n-2): how many ways to reach the stahe that only needs two steps

'''

class Solution:
    def climbStairs(self, n: int) -> int:
      # case for 0 step and 1 step
      if n == 0:
        return 0
      elif n == 1:
        return 1

      # set dynamica programming table
      # set up to n step, so initialize up to n array
      dp = [0] * (n+1) # starts from position 0, so n + 0 -> n+1 slots to store steps
      # initilize first 2 case stept(n-1), step(n-2)
      dp[0] = 1
      dp[1] = 1

      for i in range(2, n+1): # [0] [1] already set so start from [2] till [n]
        dp[i] = dp[i-1] + dp[i-2]

      return dp[n]
        
