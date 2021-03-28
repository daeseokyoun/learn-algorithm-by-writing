from typing import List
import collections

tests = {
    1: ["eat","tea","tan","ate","nat","bat"],
    2: [""],
    3: ["a"],
    4: ["ab","cd","ef"],
    5: ["abc", "bca", "cba"]
}

res = {
    # 현재 이 코드에서는 결과에 순서가 뒤섞이는 것을 실패로 확인합니다.
    # 정확한 테스트는 leetcode / GeeksForGeeks에서 진행해보는 것이 좋습니다
    1: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
    2: [[""]],
    3: [["a"]],
    4: [['ab'], ['cd'], ['ef']],
    5: [['abc', 'bca', 'cba']]
}

def is_same_2d_list(alist: List, blist: List):
    a_set = set(map(tuple, alist))
    b_set = set(map(tuple, blist))

    return a_set == b_set

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_2d_list(output, res.get(index, []))

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = collections.defaultdict(list)

    for s in strs:
        hashmap["".join(sorted(s))].append(s)

    return hashmap.values()

def main():
    for index, input_list in tests.items():
        output= groupAnagrams(input_list)

        if check_result(index, output):
            print(f'Test case {index} is correct: value {output}')
        else:
            print(f'Test case {index} is failed: value {output}')

if __name__ == '__main__':
    main()