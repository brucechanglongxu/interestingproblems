# Compute the square root of a given non-negative integer x

# Time Complexity: O(log x)
# Space COmplexity: O(1)

class Solution:
  def mySqrt(self, x: int) -> int:
    l = 1
    r = x + 1
    
    while 1 < r:
      m = (1 + r) // 2
      if m * m > x:
        r = m
      else:
        l = m + 1
        
    # l: smallest number such that l * l > x
    return l - 1
