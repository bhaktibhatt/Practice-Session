'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
'''
nums = [1,2,3,1]
#1. create hashset
# hashset = set() 
    # 2. go through every value of the list
# for n in nums: 
        # 4. check if list value n is already in hashset
    # if n in hashset:
        # print('True')
    #3.add every value of list in hashset 
#     hashset.add(n) 
# print('False')
len1 = len(nums)
len2 = len(set(nums))
print(len1)
print(len2)

