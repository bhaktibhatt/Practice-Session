nums = [1,7,3,6,5,6]
# for i in range(1,len(nums)):
#     for j in range(len(nums),1,-1):
#         nums[i]
#     nums[i] += nums[i-1]
# if nums[i] == nums[j]:
#     print(nums[i])

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