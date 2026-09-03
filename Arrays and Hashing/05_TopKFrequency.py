
# Naive Solution -> sorting

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         number_frequencies = dict()
        
#         # Get frequency of each number
#         for n in nums:
#             if n not in number_frequencies:
#                 number_frequencies[n] = 0
#             number_frequencies[n] += 1
        
#         print(f"Frequencies map: {number_frequencies}")
        
#         # Build a list of [number, frequency]
#         my_list = []
#         for number, frequency in number_frequencies.items():
#             print(f"number: {number}")
#             print(f"frequency: {frequency}")
#             my_list.append([frequency, number])
#         print("List after appending: ", my_list)
        
#         #Instead of using a list to sort the numbers we can sort the dict
        
#         sorted_dict = sorted(number_frequencies.items(), key=lambda x : x[1])
#         print(number_frequencies.items())
#         print("here",sorted_dict)
        
#         # # print(f"List before sorting: {my_list}")
        
#         my_list.sort()
#         print(f"List after sorting (by number, not frequency!): {my_list}")
        
#         result = []
        
#         for i in range(len(my_list)):
#             if len(result) == k:
#                 break
#             popped = my_list.pop()
#             # print(f"Popped element: {popped}")
            
#             result.append(popped[1])
#             # print(f"Current result: {result}")
#             # print(f"Remaining list: {my_list}")

#         # print(f"Final result: {result}")
#         return result


# instance = Solution()

# print(instance.topKFrequent(nums=[1,2,2,3,3,3,3,1,1,1,1,1,1,3,3,3,2,2,2,2,2,2], k=2))
# # print(instance.topKFrequent(nums=[7,7], k=1))


# Min Heap
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         print(f"count: {count}")
#         heap = []
#         for num in count.keys():
#             heapq.heappush(heap, (count[num], num))
#             print(f"hip after push: {heap}")
#             if len(heap) > k:
#                 heapq.heappop(heap)
#                 print(f"heap after pop: {heap}")

#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])
#         return res

# instance = Solution()

# # Heapq 

# print(instance.topKFrequent(nums=[1,2,2,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,2,2,2,2,2,2], k=2))

# Bucket Sort
""" 
1. Build a frequency map that counts how many times each number appears.
2. Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
3. For each number and its frequency in the map, add the number to freq[frequency].
4. Initialize an empty result list.
5. Loop from the largest possible frequency down to 1:
    a. For each number in freq[i], add it to the result list.
    b. Once the result contains k numbers, return it. 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a frequency map that counts how many times each number appears.
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
        frequency_bucket = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            frequency_bucket[freq].append(num)
        
        print(frequency_bucket)
            
        result = []
        
        for i in range(len(frequency_bucket ) - 1, 0 , -1):
            for num in frequency_bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
        
    
instance = Solution()
print(instance.topKFrequent(nums=[1,1,1,2,2,2,3,3,3], k=2))