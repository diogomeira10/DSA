from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = ["",""]
        return decoded_strings


instance = Solution()
def encode_and_decode(strings: List[str]) -> List[str]:
    encoded_string = instance.encode(strings)
    print(f"Encoded string: ", encoded_string)
    decoded_strings = instance.decode(encoded_string)
    print(f"Decoded string: {decoded_strings}")
    return decoded_strings


# Test cases
test_cases = [["Hello","World"],[""]]

function_results = dict()
for i,test_case in enumerate(test_cases):
    try:
        function_results[i] = encode_and_decode(test_case)
    except ValueError as err:
        print(f"FAILED TO encode_and_decode strs:{test_case} because:\n {err}")
        continue
print(f"Test Cases: {test_cases}")

test_results = {"passed": 0,"failed":0}

for input,output in function_results.items():
    if input == output:
        test_results["passed"] += 1
    else:
        test_results["failed"] += 1

print(f"{test_results.get("passed")} tests passed!")
print(f"{test_results.get("failed")} tests failed!")

