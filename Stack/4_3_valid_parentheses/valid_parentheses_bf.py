from typing import List

tests = {
    1: "()",
    2: "()[]{}",
    3: "(]",
    4: "([)]",
    5: "{[]}",
    6: "(",
    7: "]",
    8: "((){})"
}

res = {
    1: True,
    2: True,
    3: False,
    4: False,
    5: True,
    6: False,
    7: False,
    8: True
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def isValid(s: str) -> bool:
    stack = []

    paren_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch not in paren_map.keys():
            stack.append(ch)
        else:
            pair = stack.pop() if stack else ''

            if paren_map[ch] != pair:
                return False

    return len(stack) == 0

def main():
    for index, input_string in tests.items():
        res = isValid(input_string)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()