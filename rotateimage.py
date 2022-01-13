# Given an n by n 2D matrix representing an image, we will rotate the image 90 degrees clockwise

# Time Complexity : O(n^2)
# Space Complexity: O(1)

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    matrix.reverse()
    
  for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
      matrix[i][j], matrix[j][i] = matrix[j][i] = matrix[j][i], matrix[i][j]
      
class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    for min in range(len(matrix) // 2):
      max = len(matrix) - min - 1
      for i in range(min, max):
        offset = i - min
        top = matrix[min][i]
        matrix[min][i] = matrix[max - offset][min]
        matrix[max - offset][min] = matrix[max][max - offset]
        matrix[max][max - offset] = matrix[i][max]
        matrix[i][max] = top
        
        
