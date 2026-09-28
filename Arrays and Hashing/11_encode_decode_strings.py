class Solution:
    # def encode(self, strs: list[str]) -> str:

    #     if not strs:
    #         return ""

    #     res = []

    #     for string in strs:
    #         res.append(str(len(string)))
    #         res.append("#")
    #         res.append(string)

    #     return "".join(res)

    # def decode(self, s: str) -> list[str]:

    #     if not s:
    #         return []

    #     strings = []
    #     i = 0

    #     while i < len(s):
    #         j = i

    #         print(f"j{j}")
    #         print(f"s{s[j]}")

    #         while s[j] != "#":
    #             j += 1

    #         length = int(s[j - 1])
    #         j += 1
    #         word = s[j : j+length]
    #         strings.append(word)
    #         print(word)
    #         print(f"length: {length} ")
    #         i = j +length

    #     return strings
    def encode(self, strs: list[str]) -> str:

        if not strs:
            return ""

        encoded_string = []

        for string in strs:
            encoded_string.append(str(len(string)))
            encoded_string.append("#")
            encoded_string.append(string)
            print(encoded_string)

        return "".join(encoded_string)

    def decode(self, s: str) -> list[str]:

        if not str:
            return []

        i = 0
        decoded_strings = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i : j])
            j += 1
            word = s[j : j + length]
            decoded_strings.append(word)
            print(word)
            i = j + length

        return decoded_strings


instance = Solution()


def encode_and_decode(strings: list[str]) -> list[str]:
    encoded_string = instance.encode(strings)
    print("Encoded string: ", encoded_string)
    decoded_strings = instance.decode(encoded_string)
    # print(f"Decoded string: {decoded_strings}")
    return decoded_strings


test_cases = {
    1: ["Hello", "World"],
    2: [""],
    3: ["we", "say", ":", "yes", "!@#$%^&*()"]
}

tests_failed = 0
tests_passed = 0

function_results = {}
for test_case in test_cases.values():
    try:
        encoded_decoded = encode_and_decode(test_case)
    except ValueError as err:
        print(f"FAILED to encode_and_decode strs:{test_case} because:\n {err}")
        continue

    if encoded_decoded == test_case:
        tests_passed += 1
    else:
        tests_failed += 1

print(f"Test Cases: {test_cases}")


print(f"{tests_passed} tests passed!")
print(f"{tests_failed} tests failed!")
