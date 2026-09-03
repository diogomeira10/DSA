from collections import Counter

#First Solution:

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         sorted_s = list(s)
#         sorted_t = list(t)
#         sorted_s.sort()
#         sorted_t.sort()
        
#         return sorted_s == sorted_t


# Instead of using the counter class:

        # dict_s = dict()
        # dict_t = dict()
        
        # for letter in s:
        #     if letter not in dict_s:
        #         dict_s[letter] = 0
        #     dict_s[letter] += 1
            
        # for letter in t:
        #     if letter not in dict_t:
        #         dict_t[letter] = 0
        #     dict_t[letter] += 1

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False
           
#         counter_s = Counter(s)
#         counter_t = Counter(t)
        
#         # print(f"counter_s: {counter_s}")
#         # print(dict_s)
#         # print(f"counter_t: {counter_t}")
        

#         # print(dict_t)
        
#         for letter in counter_s:
#             if letter in counter_t:
#                 if counter_s[letter] != counter_t[letter]:
#                     return False
#             else:
#                 return False
                
#         return True
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False
           
        

        
#         return sorted(s) == sorted(t)
            
        

# solution_1 = Solution()

# print(solution_1.isAnagram(s = "anagram", t = "nagaram"))
# print(solution_1.isAnagram(s = "rat", t = "car"))





# class Solution:
#     def isAnagram(self,s,t):
        
        
#         pass
    


""" Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false """

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False
           
#         counter_s = Counter(s)
#         counter_t = Counter(t)
        
#         for letter in counter_s:
#             if letter in counter_t:
#                 if counter_s[letter] != counter_t[letter]:
#                     return False
#             else:
#                 return False
                
#         return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         if(len(s) != len(t)): 
#             return False
        
#         # contar as occurencias de cada letra em cada palavra
        
#         word_s = dict()
#         word_t = dict()        
        
#         for letter in s:
#             if letter not in word_s:
#                 word_s[letter] = 0
#             word_s[letter] += 1
            
#         for letter in t:
#             if letter not in word_t:
#                 word_t[letter] = 0
#             word_t[letter] += 1
            
#         print(word_s)
#         print(word_t)
            
#         return word_s == word_t
            
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)): 
            return False
        
        # contar as occurencias de cada letra em cada palavra
        
        word_s = dict()
        word_t = dict()        
        
        for i in range(len(s)):
            word_s[s[i]] = 1 + word_s.get(s[i], 0)
            word_t[t[i]] = 1 + word_t.get(t[i], 0)
        
        
            
        print(word_s)
        print(word_t)
            
        return word_s == word_t
    
# Exercise => Determine Time and Space Complexity

# TC - How the number of operations increase as input increases.
# SC - How the space increases as input increases  

# TC - 
# SC - O(1)
          

        
        
        
        
solution_1 = Solution()      
print(solution_1.isAnagram(s = "anagram", t = "nagaram"))
print(solution_1.isAnagram(s = "rat", t = "car"))



