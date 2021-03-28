from typing import List
import collections

tests = {
    1: "abc"
}

res = {
    1: ["abc", "acb", "bac", "bca", "cab", "cba"]
}

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_list(output, res.get(index, []))

def find_permutation(res, chs, s, e):
    if s == e - 1:
        res.append("".join(chs))
    else:
        for i in range(s, e):
            chs[s], chs[i] = chs[i], chs[s]
            find_permutation(res, chs, s + 1, e)
            chs[s], chs[i] = chs[i], chs[s] 

def main():
    for index, input_str in tests.items():
        res = []
        find_permutation(res, list(input_str), 0, len(input_str))

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()