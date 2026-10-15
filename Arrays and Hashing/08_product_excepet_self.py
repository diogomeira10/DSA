# Brute force
# Nested for loop
from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         n = len(nums)

#         products: List[int] = list()

#         for i in range(n):
#             product = 1
#             for j in range(n):
#                 if i == j:
#                     continue
#                 product *= nums[j]

#             products.insert(i, product)

#         return products

# instance = Solution()

### Test cases

# print(instance.productExceptSelf([1,2,4,6]))
# print(instance.productExceptSelf([-1,0,1,2,3]))

# Division
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         product = 1
#         zero_count = 0

#         for num in nums:
#             if num:
#                 product *= num
#             else:
#                 zero_count += 1

#         if zero_count > 1:
#             return [0] * len(nums)

#         products = [0] * len(nums)

#         for i, num in enumerate(nums):
#             if zero_count:
#                 products[i] = 0 if num else product
#             else:
#                 products[i] = product // num

#         return products


# instance = Solution()
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            

        products = []
        
        if zero_count:
            for num in nums:
                products.append(0) if num else products.append(product)
        else:
            for num in nums:
                products.append(product // num)

        return products
   
#Prefix Sufix Solution 
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        product = 1
        has_zero = False

        for num in nums:
            if num != 0:
                product *= num
            else:
                has_zero = True
        print(product)

        products = []
        
        if has_zero:
            for num in nums:
                products.append(0) if num else products.append(product)
        else:
            for num in nums:
                products.append(product // num)

        return products


instance = Solution()


# print(instance.productExceptSelf([1,2,4,6]))
# print(instance.productExceptSelf([-1, 0, 1, 2, 3]))
print(instance.productExceptSelf([0,0]))
