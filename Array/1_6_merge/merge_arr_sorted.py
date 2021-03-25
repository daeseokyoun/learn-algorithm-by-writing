from typing import List
import collections

tests = {
    # (nums1, m, nums2, n)
    1: ([1, 2, 3], 3, [], 0),
    2: ([0, 0, 0], 0, [1, 2, 3], 3),
    3: ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3),
    4: ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
}

res = {
    1: [1, 2, 3],
    2: [1, 2, 3],
    3: [1, 2, 3, 4, 5, 6],
    4: [1, 2, 3, 4, 5, 6]
}

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i, v in enumerate(nums2):
        nums1[m + i] = v

    nums1[:] = sorted(nums1)

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_list(output, res.get(index, []))

def main():
    for index, data in tests.items():
        nums1 = data[0]
        m = data[1]
        nums2 = data[2]
        n = data[3]
        merge(nums1, m, nums2, n)

        if check_result(index, nums1):
            print(f'Test case {index} is correct: value {nums1}')
        else:
            print(f'Test case {index} is failed: value {nums1}')

if __name__ == '__main__':
    main()