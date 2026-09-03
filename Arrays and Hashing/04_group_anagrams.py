# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         def isAnagram( s: str, t: str) -> bool:
#             if len(s) != len(t):
#                 return False           
#             return sorted(s) == sorted(t)
        
#         result = list()

#         for i in range(len(strs)):
#             anagrams = set()
#             for j in range(i+1, len(strs)):
#                 if isAnagram(s=strs[i], t=strs[j]):
#                     print(strs[i])
#                     anagrams.add(strs[i])
#                     anagrams.add(strs[j])
#             if(len(anagrams) > 0):
#                 result.append(list(anagrams))
        
#         return result
    

#Most readable
# from collections import defaultdict
# from typing import List
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:      
        
#         occs = defaultdict(list) 

#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             occs[sorted_word].append(word)       
            
#         for group in occs.values():
#             print("group", group)
        
        
#         return  sorted(occs.values(), key=len)


# instance = Solution()


# print(instance.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
# output = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# [['hat'], ['act', 'cat'], ['pots', 'tops', 'stop']]

# print(instance.groupAnagrams(["x"]))
# Output: [["x"]]
# print(instance.groupAnagrams([""]))
# Output: [[""]]


# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                print(count)
                print(f"calcule: {ord(c) - ord('a')}")
            print("break")
            res[tuple(count)].append(s)
        return list(res.values())
    
    
instance = Solution()


print(instance.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
output = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
[['hat'], ['act', 'cat'], ['pots', 'tops', 'stop']]

