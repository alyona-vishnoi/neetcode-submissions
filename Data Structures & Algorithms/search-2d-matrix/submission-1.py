class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we could do binary search on each row but thats mlogn
        # we can use the fact that the first int of next row is > last int of prev row
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1
        # find which row to do binary search in

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: # last elem
                top = row + 1
            elif target < matrix[row][0]: # first element 
                bot = row - 1
            else:
                break # in bounds we are good. 
        
        # if we didnt break out ie we couldnt find a row that 
        # could fit target
        if not (top <= bot):
            return False

        # now do binary search in the row we found
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

        