from typing import List
import collections

tests = {
    1: ([1,2,3,4,5,6,7], 3),
    2: ([1, 2], 3)
}

res = {
    1: [5,6,7,1,2,3,4],
    2: [2, 1]
}

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_list(output, res.get(index, []))

def rotate(nums: List[int], k: int) -> None:
    temp = [0] * len(nums)

    for i, elem in enumerate(nums):
        temp[(i + k) % len(nums)] = nums[i]

    nums[:] = temp

def main():
    for index, data in tests.items():
        nums = data[0]
        k = data[1]
        rotate(nums, k)

        if check_result(index, nums):
            print(f'Test case {index} is correct: value {nums}')
        else:
            print(f'Test case {index} is failed: value {nums}')

if __name__ == '__main__':
    main()