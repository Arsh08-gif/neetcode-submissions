class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            start = 0
            end = m - 1
            while (start <= end):
                print(start)
                print(end)
                mid = (start+end)//2
                print(mid)
                if matrix[i][mid] == target : return True
                elif matrix[i][mid] > target : end = mid-1
                else : start = mid+1
            

        return False


# [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
#  target = 10