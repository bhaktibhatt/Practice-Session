lst = [1,2,3,4]
# print(lst)
# lst[3] = lst[0]+lst[1]+lst[2]+lst[3]
# lst[2] = lst[0]+lst[1]+lst[2]
# lst[1] = lst[0]+lst[1]
# print(lst)

def running_sum(lst):
    for i in range(1,len(lst)):
        lst[i]+=lst[i-1]
    return lst
print(lst)
print(running_sum(lst))