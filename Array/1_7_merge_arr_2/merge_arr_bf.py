from typing import List
import collections

tests = {
    # (nums1, m, nums2, n)
    1: ([10], 1, [2,3], 2),
    2: ([2, 8, 10], 3, [5], 1),
    3: ([1, 4, 7, 8, 10], 5, [2, 3, 9], 3)
}

res = {
    1: ([2], [3,10]),
    2: ([2, 5, 8], [10]),
    3: ([1, 2, 3, 4, 7], [8, 9, 10]),
}

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i, nums1_item in enumerate(nums1):
        if nums1_item > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item
            
            k = 1
            while k < n and nums2[k] < nums1_item:
                nums2[k - 1] = nums2[k]
                k += 1
            nums2[k - 1] = nums1_item

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, nums1: List, nums2):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    result = res.get(index, None)

    if not result:
        raise ValueError(f'No test case no. {index}')

    nums1_res = result[0]
    nums2_res = result[1]
    return is_same_list(nums1_res, nums1) and \
           is_same_list(nums2_res, nums2)

def main():
    for index, data in tests.items():
        nums1 = data[0]
        m = data[1]
        nums2 = data[2]
        n = data[3]
        merge(nums1, m, nums2, n)

        if check_result(index, nums1, nums2):
            print(f'Test case {index} is correct: value {nums1} and {nums2}')
        else:
            print(f'Test case {index} is failed: value {nums1} and {nums2}')

if __name__ == '__main__':
    main()