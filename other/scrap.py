def roman_to_int(s: str) -> int:
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    prev_value = 0
    for c in s[::-1]:
        curr_value = roman_values[c]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value
    return result


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        n = len(arr2)
        for i in range(1, n-1, 1): # traverse arr2
        #     # for j in range(1, n-1, 1): #traverse arr1     
            if arr1[i] === arr2[i]:
                continue
            else:
                arr1.insert(0, )
