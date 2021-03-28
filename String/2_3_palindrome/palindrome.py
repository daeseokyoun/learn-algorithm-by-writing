from typing import List

tests = {
    1: "A man, a plan, a canal: Panama",
    2: "race a car",
    3: "Abbc, cbb a",
    4: ",   , --",
    5: "Abbc, cdd a"
}

res = {
    1: True,
    2: False,
    3: True,
    4: True,
    5: False
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1

    s = s.lower()

    while i < j:
        while i < j:
            if s[i].isalnum():
                break
            i += 1

        while i < j:
            if s[j].isalnum():
                break
            j -= 1

        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True

def main():
    for index, input_string in tests.items():
        res = isPalindrome(input_string)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()