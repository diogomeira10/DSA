class Solution:
    def encode(self, strs: list[str]) -> str:

        encoded_string = ""

        for string in strs:
            encoded_string += f"{len(string)}#{string}"

        print(encoded_string)
        return encoded_string



    def decode(self, s: str) -> list[str]:

        decoded_strings = []

        i, j = 0, 0

        while(i < len(s)):
            
            j = i
            
            while s[j] != "#":
                j += 1
            
            length = int(s[i: j])
            
            # j += 1
            # i = j + word_length
            # word = s[j : i]
            # decoded_strings.append(word)
            i = j + 1
            j = i + length
            word = s[i : j]
            decoded_strings.append(word)
            print(word)
            print(s)
            print("j", j)
            i = j

            
        print(f"decoded_strings:{decoded_strings}")

        return decoded_strings


instance = Solution()
str_list = ["Hello", "World"]

# strs=["we","say",":","yes","!@#$%^&*()"]
# strs=["#","##"]


encoded_list = instance.encode(str_list)
print(encoded_list)
decoded_list = instance.decode(encoded_list)
print(decoded_list)
