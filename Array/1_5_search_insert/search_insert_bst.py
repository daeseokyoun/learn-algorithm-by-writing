from typing import List

tests = {
    1: ([1, 3, 5, 6], 0),
    2: ([1, 3, 5, 6], 100)
}
res = {
    1: 0,
    2: 4
}

def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return output == res.get(index, -1)

def main():
    for index, data in tests.items():
        input_list = data[0]
        target_num = data[1]
        pos = searchInsert(input_list, target_num)

        if check_result(index, pos):
            print(f'Test case {index} is correct: value {pos}')
        else:
            print(f'Test case {index} is failed: value {pos}')

if __name__ == '__main__':
    main()