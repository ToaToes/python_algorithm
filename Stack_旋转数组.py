'''
一个数组A中存有 n 个整数，在不允许使用另外数组的前提下，将每个整数循环向右移 M（ M >=0）个位置，
即将A中的数据由（A0 A1 ……AN-1 ）变换为（AN-M …… AN-1 A0 A1 ……AN-M-1 ）（最后 M 个数循环移至最前面的 M 个位置）。
如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？

输入：
6,2,[1,2,3,4,5,6]

返回值：
[5,6,1,2,3,4]

'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
class Solution:
    def solve(self , n: int, m: int, a: List[int]) -> List[int]:
      m = m % n # 得余数 避免m > n好几轮 余数为最少需要挪得位置

      return a[-m:] + a[:-m] # from -m to end + form start to -m(not included)
