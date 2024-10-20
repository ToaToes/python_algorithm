'''
有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。

给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵。


[[1,2,3],         [[7,4,1]
[4,5,6],   ->      [8,5,2] 
[7,8,9]]           [9,6,3]]

'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param mat int整型二维数组 
# @param n int整型 
# @return int整型二维数组
#
class Solution:
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here

        res = []
        tmp = list(zip(*mat))
        for i in range(n):
            res.append(list(tmp[i])[::-1])
        return res
