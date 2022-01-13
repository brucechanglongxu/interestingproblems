class Solution:
  def minSideJumps(self, obstacles: List[int]) -> int:
    kInf = 1e6
    
    # dp[i] := minimum jump to reach lane i
    dp = [kInf, 1, 0, 1]
    
    for obstacle in obstacles:
      print(dp)
      if obstacle > 0:
        dp[obstacle] = kInf
       for i in range(1, 4): # current
        for i != obstacle:
          for j in range(1, 4): # previous
            dp[i] = min(dp[i], dp[j] + (0 if i == j else 1))
            
    return min(dp)