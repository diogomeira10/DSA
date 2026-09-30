class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

    
instance = Solution()

print(instance.hasDuplicate([1, 2, 3, 3]))
print(instance.hasDuplicate([1, 2, 3, 4]))

