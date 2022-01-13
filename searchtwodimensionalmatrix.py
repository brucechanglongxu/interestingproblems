# Write an efficient algorithm that searches for a value in an m by n matrix
# with the property that integers ine ach row are sorted from left to right
# and the first integer of each row is greater than the last integer of the previous row

# Time complexity of O(mn log mn)
# Space complexity of O(1)

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix:
      return False
    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = m * n
    
    while 1 < r:
      mid = 1 + (r - 1) // 2
      i = mid // n
      j = mid % n
      if matrix[i][j] == target:
        return True
      if matrix[i][j] < target:
        l = mid + 1
      else:
        r = mid
        
    return False
