from typing import List

# Works for positive numbers only. Negatives fail because
# I dont have a way to index -1 for example.
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         if not nums:
#             return 0
    
#         numbers = list(set(nums))
#         numbers.sort()
        
#         maximum_number = max(numbers)
        
#         digits = [False] * (maximum_number + 1)
#         print(digits)
        
#         for n in numbers:
#                 digits[n] = n
#         print(digits)
           
#         sequences = []
#         count = 0
        
#         for n in digits:
#              if not n and count > 1:
#                  sequences.append(count)
#                  count = 0
#                  continue
#              if str(n).isdigit():
#                 count+=1
#              if n == maximum_number:
#                 sequences.append(count)
        
#         return max(sequences) if sequences else 0               
            
# instance = Solution()


#Idea -> store the begginings of sequences
## Too slow, does not work with bigger numbers
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         if not nums:
#             return 0
    
#         numbers = list(set(nums))
#         numbers.sort()
        
#         if len(numbers) == 1:
#             return 1
        
#         begginings_of_sequences = list()
        
#         for number in numbers:
#             smaller = number - 1
#             if smaller not in numbers:
#                 begginings_of_sequences.append(number)
#         # print(f"beggings {begginings_of_sequences}")
        
#         sequences = list()
#         count = 0
        
#         # print("ordered_list", numbers)
#         # print(begginings_of_sequences)
        
        
#         for index,number in enumerate(numbers):
#             if number in begginings_of_sequences:
#                 if count:
#                     sequences.append(count)
#                     count = 0 
#                     count += 1
#                 else:
#                     count+=1
#             else:
#                 if index == len(numbers) -1 :
#                     count += 1
#                     sequences.append(count)
#                 if count:
#                     count+=1
#         # print("sequences", sequences)
            
#         # print(count)
        
#         return max(sequences)
                    
          
            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
    
        numSet = set(nums)
        
        if len(numSet) == 1:
            return 1
        
        longest = 0
        
        for num in numSet:
            if num - 1 not in numSet:
                length = 0
                while (num + length in numSet):
                    length += 1 
                if length > longest:
                    longest = length
                    
        return longest                    
                    
                    
          
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        numSet = set(nums)
        
        if len(numSet) == 1:
            return 1
        
        max_sequence = 0
        
        for n in numSet:
            if n - 1 not in numSet: # is an initial
                length = 0
                # Tenho de fazer o processo onde eu encontro sequencialment se existe um numero maior que 1 do atual;
                while(n + length in numSet):
                    length += 1
                
                if length > max_sequence:
                    max_sequence = length
        
        return max_sequence
            
            
instance = Solution()



nums = [2,20,4,10,3,4,5]
print(instance.longestConsecutive(nums))
nums = [0,3,2,5,4,6,1,1]
print(instance.longestConsecutive(nums))
nums=[0,-1]
print(instance.longestConsecutive(nums))
nums=[0,0]
print(instance.longestConsecutive(nums))
