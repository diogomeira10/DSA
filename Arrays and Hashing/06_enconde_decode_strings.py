class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            print(len(string))
            encoded_string += str(len(string)) + "#" + string
        # print(f"encode string: {encoded_string}")
        
        return encoded_string.encode()


    def decode(self, s: str) -> List[str]:
        
        i = 0
        decoded = s.decode()

        curr_len = 0
        
        for i in range(len(decoded)):
            char = decoded[i]
            if char == "#":
                curr_len = int(decoded[i + 1])
                
                
        

        return
    
instance = Solution()
str_list = ["Hello", "World"]


encoded_list = instance.encode(str_list)
print(encoded_list)
decoded_list = instance.decode(encoded_list)
print(decoded_list)

# str_list = ["Hello World", "Test"]

# encoded_list = instance.encode(str_list)
# print(encoded_list)
# decoded_list = instance.decode(encoded_list)
# print(decoded_list)




# Test env

# text = "string"
# encoded_string = text.encode()
# decoded_string = encoded_string.decode()
# print(text)
# print(encoded_string)
# print(decoded_string)

# print(text + "s")
# print("" + "s")

# hello_world = "Hello World"
# print(hello_world.encode())