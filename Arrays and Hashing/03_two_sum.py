# BruteForce
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
 
 
#Two Pointers:       
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         sorted_nums = sorted(nums)
#         start = 0
#         end = len(nums) - 1
        
#         while start < end:
#             sum = sorted_nums[start] + sorted_nums[end]
#             if sum == target:
#                 return [start, end]
#             elif sum < target:
#                 start += 1
#             else:
#                 end -=1
   
#         return []
      
      
      
# Hash map (Two Pass) 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         value_index = dict()
        
#         for index,value in enumerate(nums):
#             value_index[value] = index    
      
#         for index,num in enumerate(nums):
#             complement = target - num
#             if complement in nums and index != value_index[complement]:
#                 return [index, value_index[complement]]
   
#         return []

#Hash Map (One pass)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         value_index = dict()
        
#         for index,value in enumerate(nums):
#             diff = target - value
#             if diff in value_index:
#                 return [index, value_index[diff]]
            
#             value_index[value] = index
   
#         return []
        
# instance = Solution()

# print(instance.twoSum(nums=[4,5,6], target=10))
# print(instance.twoSum(nums=[3,4,5,6], target=7))
# print(instance.twoSum(nums=[5,5], target=10))

# Input: 
# nums = [3,4,5,6], target = 7


#Hash Map (One pass)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
#         my_dict = dict()
        
#         for index, num in enumerate(nums):
#             diff = target - num  
            
#             if diff in my_dict:
#                 return [my_dict[diff],index]
               
#             my_dict[num] = index
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        occs = dict()
        
        for i,n in enumerate(nums):
            rest = target - n
            print(rest)
            
            if occs.get(rest):
                return [occs[rest],i]
            else:
                occs[n] = i
        print(occs)
        
                

        
            
        
        
instance = Solution()

print(instance.twoSum(nums=[4,5,6], target=10))
print(instance.twoSum(nums=[3,4,5,6], target=7))
print(instance.twoSum(nums=[5,5], target=10))