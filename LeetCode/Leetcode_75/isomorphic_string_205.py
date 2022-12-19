'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false
'''
#? what is isomorphic?
#? first check the len of 2 strings if they are equal then map s char to t and 
#? e -> a , g -> d these character dont map to any other character and mapping goes both ways

#! check that key exists and is not already a part of any map
#! also verify that s char is not again in t i.e mapping both ways
#! if the current char as key is seen map then we will return false else true

#* when len is same we run for loop

# * c1=e , c2=a
# *check e in map1 and map1[e] not a OR check a in map2 and map2[a] not e  <== if this is true return False
#* next the above is not true as e and a first occurence hence, we do
#* map1[e] = a , map2[a] = e ==> Return True

#* c1 = g , c2 = d
#* check g in map1 (not there) and map1[g] not d (i.e already exists)  OR  d in map2 and map2[d] not g
#* the above is not true as g and d are encountered for first time
#* then, map1[g] = d and map2[d] = g ==> Return True

#* c1 = g , c2 = d
#* check g in map1 (not there) and map1[g] not d (i.e already exists)  OR  d in map2 and map2[d] not g
#* in above the mapping exists and the key also exist so the if will not execute
#* then, map1[g] = d and map2[d] = g ==> Return True

s = 'egg'
t = 'add'
a = 'xyz'
def isIsomorphic(s,t):
    map1,map2  = {},{}
    if (len(s) != len(t)):
        return False
    else:
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if((c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1)):
                return False
            map1[c1] = c2
            map2[c2] = c1
        return True

print(isIsomorphic(s,a))
                    