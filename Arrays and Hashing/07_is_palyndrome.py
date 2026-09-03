## Reverse String Solution

# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         cleaned_string = ""

#         for char in s:
#             if char.isalnum():
#                 cleaned_string += char.lower()
        
#         return cleaned_string == cleaned_string[::-1]
    



# instance = Solution()


## Two Pointers Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        p1, p2 = 0, len(s)- 1
        
        # enquanto p1 menor que p2
        # ver se isalnum 
        
        while p1 < p2:
            p1_char = s[p1]
            p2_char = s[p2]
                        
            if not p1_char.isalnum():
                p1 += 1
                continue
            if not p2_char.isalnum():
                p2 -= 1
                continue
                
            if p1_char.lower() != p2_char.lower():
                print(p1_char.lower())
                print(p2_char.lower())
                return False
            
            p1 += 1
            p2 -= 1
            

        
        return True
                

instance = Solution()

print(instance.isPalindrome("Was it a car or a cat I saw?"))
print(instance.isPalindrome("tab a cat"))
