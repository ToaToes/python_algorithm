'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

# Simply just to use a Hash table to get unique key

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        hash_table = {}

        for i in nums:
            hash_table[i] = i

        nums = list(hash_table.keys())

        return len(hash_table)    

'''
# Get all keys
keys = hash_table.keys()

# Convert to list if needed
keys_list = list(keys)
'''



'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.


Same way to solve as above
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hash_table = {}

        for i in range(len(nums)):
            if nums[i] != val:
                hash_table[i] = nums[i]

        nums = list(hash_table.values())

        return len(nums)
