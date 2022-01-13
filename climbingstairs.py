# Find the total number of ways it takes to climb n stairs if we have the option
# of climbing either one or two steps each time. Dynamic Programming Solution

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution1:
  def climbStairs(self, n: int) -> int:
    # dp[i] := # of distinct ways to climb the i-th stair
    dp = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
  
  class Solution2:
    def climbStairs(self, n: int) -> int:
      prev1 = 1 # dp[i - 1]
      prev2 = 1 # dp[i - 2]
      
      for i in range(2, n + 1):
        dp = prev1 + prev2
        prev2 = prev1
        prev1 = dp
        
      return prev1
