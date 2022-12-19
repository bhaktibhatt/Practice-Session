'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

lst = [1,2,3,4]
# print(lst)
# lst[3] = lst[0]+lst[1]+lst[2]+lst[3]
# lst[2] = lst[0]+lst[1]+lst[2]
# lst[1] = lst[0]+lst[1]
# print(lst)
# l[1] = l[1]+l[0] = 1+2 ==> l[1]=3, 
# l[2] = l[2]+l[1] = 3+3 ==> l[2] = 6, 
# l[3] = l[3]+l[2] = 4+6 ==> l[3] = 10 
# and stop
def running_sum(lst):
    for i in range(1,len(lst)): #check till 1 to 4 
        lst[i]+=lst[i-1]  
    return lst
print(lst)
print(running_sum(lst))