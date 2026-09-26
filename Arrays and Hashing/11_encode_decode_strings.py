from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""

        res = []

        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        strings = []
        i = 0

        while i < len(s):
            j = i
            
            print(f"j{j}")
            print(f"s{s[j]}")

            while s[j] != "#":
                j += 1

            length = int(s[j - 1])
            j += 1
            word = s[j : j+length]
            strings.append(word)
            print(word)
            print(f"length: {length} ")
            i = j +length

        return strings


instance = Solution()


def encode_and_decode(strings: List[str]) -> List[str]:
    encoded_string = instance.encode(strings)
    print("Encoded string: ", encoded_string)
    decoded_strings = instance.decode(encoded_string)
    # print(f"Decoded string: {decoded_strings}")
    return decoded_strings


test_cases = {
    1: ["Hello", "World"],
    2: [""]
}

tests_failed = 0
tests_passed = 0

function_results = {}
for test_case in test_cases.values():
    try:
        encoded_decoded = encode_and_decode(test_case)
    except ValueError as err:
        print(f"FAILED TO encode_and_decode strs:{test_case} because:\n {err}")
        continue

    if encoded_decoded == test_case:
        tests_passed += 1
    else:
        tests_failed += 1

print(f"Test Cases: {test_cases}")


print(f"{tests_passed} tests passed!")
print(f"{tests_failed} tests failed!")

# A good software design is the one that can be changed easily


###Recursive
# Onde e que estou
# Fazer o minimo passo possivel para atingir onde quero estar
# Ver se parti alguma coisa e corrigir.
# Repete

f = "2"
if f.isdigit():
    print("yes")
else:
    print("No")


sss = "DiogoMeira"
print(sss[1:3])
