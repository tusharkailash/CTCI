# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
# place?

class Solution(object):
    def rotate90(self,matrix):
        n = len(matrix)
        for layer in range(0,(n+1)/2):
            first = layer
            last = n-layer-1

            for i in range(first,last):
                offset = i-first
                temp = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = temp
        return matrix


matrix = [[1,2,3,4],[ 4,5,6,7],[6,8,6,5],[0,-1,4,2]]
print Solution().rotate90(matrix)

#Working of the code:
# layer range -> 0,1
#
# LAYER=0:
# first = 0 , last = 3
# Therefore, i = 0,1,2
# When i=0:  offset = 0-0 = 0
#            matrix[0][0] = matrix[3][0]
#            matrix[3][0] = matrix[3][3]
#            matrix[3][3] = matrix[0][3]
#            matrix[0][3] = matrix[0][0]
#
#
# When i=1:  offset = 1-0 = 1
#            matrix[0][1] = matrix[2][0]
#            matrix[2][0] = matrix[3][2]
#            matrix[3][2] = matrix[1][3]
#            matrix[1][3] = matrix[0][1]
#
# When i=0:  offset = 2-0 = 2
#            matrix[0][2] = matrix[1][0]
#            matrix[1][0] = matrix[3][1]
#            matrix[3][1] = matrix[2][3]
#            matrix[2][3] = matrix[0][2]
#
# LAYER=1
# first = 1 , last = 4-1-1 = 2
# Therefore, i = 1
#
# When i=1:  offset = 1-1 =0
#            matrix[1][1] = matrix[2][1]
#            matrix[2][1] = matrix[2][2]
#            matrix[2][2] = matrix[1][2]
#            matrix[1][2] = matrix[1][1]
#
