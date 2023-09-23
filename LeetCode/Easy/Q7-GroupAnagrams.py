'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)
for s in strs:
    count = [0] * 26 #a ... z
    for c in s:
        count[ord(c) - ord("a")] += 1
    res[tuple(count)].append(s)
print(res.values())

