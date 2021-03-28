from typing import List
import sys

tests = {
    1: [1,5,11,5],
    2: [1,2,3,5],
    3: [3, 2, 4, 7, 1]
}

res = {
    1: 0,
    2: 1,
    3: 1 
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, -1) == output

min_diff = float('inf')
total = 0

def subset_diff(index: int, nums: List[int], subsum: int):
    global total, min_diff
    if index == len(nums):
        min_diff = min(min_diff, abs(((total - subsum) - subsum)))
        return

    subset_diff(index + 1, nums, subsum + nums[index])
    subset_diff(index + 1, nums, subsum)

def main():
    global total, min_diff
    for index, arr in tests.items():
        min_diff = float('inf')
        total = sum(arr)
        subset_diff(0, arr, 0)

        if check_result(index, min_diff):
            print(f'Test case {index} is correct: value {min_diff}')
        else:
            print(f'Test case {index} is failed: value {min_diff}')

if __name__ == '__main__':
    main()