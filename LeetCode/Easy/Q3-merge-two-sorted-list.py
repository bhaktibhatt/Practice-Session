'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
# '''
# l1 = [1,2,4]
# l2 = [1,3,4]
# l3 = sorted((l1) + (l2))
# print(sorted(l3))
# '''
'''
def myLst(n,m):
    l1 = []
    l2 = []
    for x in range (n):
        i = int(input("val:"))
        l1.append(i)
    for y in range(m):
        j = int(input("val1:"))
        l2.append(j)
    print(l1)
    print(l2)
    l3 = sorted(l1+l2)
    print(l3)

myLst(3,3)
'''
 
def mySortedList():
    l1 = [1,2,4]
    l2 = [1,3,4]
    for x in range(len(l1)):
        for y in range(len(l2)):
            l3 = sorted(l1+l2)
    print(l3)

mySortedList()

# TypeError: object of type 'ListNode' has no len()
#     for x in range(len(list1)):
# Line 8 in mergeTwoLists (Solution.py)
#     ret = Solution().mergeTwoLists(param_1, param_2)
# Line 35 in _driver (Solution.py)
#     _driver()
# Line 46 in <module> (Solution.py)

'''
well.... you have to use a linked list for this problem 🙂
okay so..
a singly linked list is made up of node that contains a data val and a pointer to the next node
i need to create a node first!
'''
class Node:
    def __init__(self,data= 0, next = None): #data = data field on create nodes not linked 
        self.data = data
        self.next = next #next is the link 


print(n1.self.data)
# class LinkedList:
#     def __init__(self):
#         self.head =None #empty linked list
