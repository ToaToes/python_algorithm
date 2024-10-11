'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Use a binary search to solve, have one or two pivot to track
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # To sovle case like: [1], target: 1
        if target in nums:
            return nums.index(target)
     
        left = 0
        right = len(nums)-1

        #eliminate the biggest or smallest case
        if(nums[right] < target):
            return right+1
        elif(nums[left] > target):
            return left

        #update the pivot for track down in-between case
        while left < right:
            mid = (right + left)//2 #to get the left flooring num

            if(right - left == 1):
                return right

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
