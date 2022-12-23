nums = [1,7,3,6,5,6]
#! here we will take sum(nums) = 28

#* at nums[0]
#? rs = 28 - nums[0] - 0 ==> rs = 28-1-0 = 27
#? check if ls = rs ? no : then pass
#? ls = ls + nums[0] = 0+1 = 1

#* at nums[1]
#? rs = 28 - nums[1] - ls ==> 28 - 7 - 1 = 20
#? rs != ls hence pass
#? ls = ls + nums[1] ==> 1 + 7 = 8

#* at nums[2]
#? rs = 28 - nums[2] - ls ==> 28 - 3 - 8  ==> 17
#? rs != ls hence pass
#? ls = ls + nums[2] ==> 8 + 3 ==> 11

#* at nums[3]
#? rs = 28 - nums[3] - ls ==> 28 - 6 - 11 ==> 11
#! now rs == ls
#? return index i.e 3 i.e 3 index is pivot

#! if left_sum == right_sum at a particular index val then that index is pivot index

def pivotIndex(nums):
    total = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if rightSum == leftSum:
            return i
        leftSum += nums[i]
    return -1

print(pivotIndex(nums))