# Hashmap을 이용한 방법
# Brute Force 방법으로 문제 풀이
from typing import List
import collections

tests = {
    1: ([2, 7, 8, 11], 9)
}
res = {
    1: [0, 1]
}

# hashmap으로 저장하여 target 조합의 인덱스를 찾는다
# hashmap의 키로 배열의 요소를 사용하고, 값으로는 해당 요소의 인덱스를 저장한다.
def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable_dict = {}

    for i in range(0, len(nums)):
        value = target - nums[i]

        if hashtable_dict.get(value) is not None \
            and hashtable_dict[value] != i:
            return sorted([i, hashtable_dict[value]])

        hashtable_dict[nums[i]] = i

    return [-1, -1]

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_list(output, res.get(index, []))

def main():
    for index, data in tests.items():
        input_list = data[0]
        target_num = data[1]
        output = twoSum(input_list, target_num)

        if check_result(index, output):
            print(f'correct answer {output} for', end=' ')
        else:
            print(f'wrong answer {output} for', end=' ')
        print(f'the input nums {input_list} and target {target_num}')

if __name__ == '__main__':
    main()