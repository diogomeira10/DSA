from typing import List

# Works for positive numbers only. Negatives fail because
# I dont have a way to index -1 for example.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
    
        numbers = list(set(nums))
        numbers.sort()
        
        maximum_number = max(numbers)
        
        digits = [False] * (maximum_number + 1)
        print(digits)
        
        for n in numbers:
                digits[n] = n
        print(digits)
           
        sequences = []
        count = 0
        
        for n in digits:
             if not n and count > 1:
                 sequences.append(count)
                 count = 0
                 continue
             if str(n).isdigit():
                count+=1
             if n == maximum_number:
                sequences.append(count)
        
        return max(sequences) if sequences else 0               
            
instance = Solution()


#Idea -> store the begginings of sequences
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
    
        numbers = list(set(nums))
        numbers.sort()
        
        maximum_number = max(numbers)
        
        digits = [False] * (maximum_number + 1)
        print(digits)
        
        for n in numbers:
                digits[n] = n
        print(digits)
           
        sequences = []
        count = 0
        
        for n in digits:
             if not n and count > 1:
                 sequences.append(count)
                 count = 0
                 continue
             if str(n).isdigit():
                count+=1
             if n == maximum_number:
                sequences.append(count)
        
        return max(sequences) if sequences else 0               
            
instance = Solution()



# nums = [2,20,4,10,3,4,5]
# print(instance.longestConsecutive(nums))
# nums = [0,3,2,5,4,6,1,1]
# print(instance.longestConsecutive(nums))
nums=[0,-1]
print(instance.longestConsecutive(nums))
