'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other. 

'''

''''
write approach here
1. Create a defaultdict to hold lists of anagrams.
2. Iterate through each string in the input list.
3. Sort the string to create a key that represents its anagram group.
4. Append the original string to the list corresponding to the sorted key in the defaultdict.
5. Finally, return the values of the defaultdict as a list of lists.
6. Time complexity is O(n * k log k) where n is the number of strings and k is the maximum length of a string.

write sudocode here
1. Initialize a defaultdict called anagrams to hold lists.
2. For each string s in the input list strs:
3.    Sort the string s to create a key.
4.   Append s to the list in anagrams corresponding to the key.
5. Return the list of values from anagrams.
6. Time complexity is O(n * k log k) where n is the number of strings and k is the maximum length of a string.
  
'''


from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    print(anagrams)
    
    for s in strs:
        # Sort the string to get the anagram key
        key = ''.join(sorted(s))
        print(key)
        anagrams[key].append(s)
        print(anagrams)
    
    return list(anagrams.values())

result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)