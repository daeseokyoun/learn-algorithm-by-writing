from typing import List
import re

tests = {
    1: "172.16.20.2",
    2: "2001:0db8:85a3:0:0:8A2E:0370:7334",
    3: "256.256.256.256",
    4: "2001:0db8:85a3:0:0:8A2E:0370:7334:",
    5: "123.123.123.123.",
    6: "0.0.0.0",
    7: "20AB:Fb8:85a3:0:0:8A2E:0370:7334"
}

res = {
    1: "IPv4",
    2: "IPv6",
    3: "Neither",
    4: "Neither",
    5: "Neither",
    6: "IPv4",
    7: "IPv6"
}

def check_result(index: int, output: str):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, "") == output

def validIPAddress(IP: str) -> str:
    IPV4 = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'

    ipv4 = \
        re.compile(r'^({p}\.){{3}}{p}$'.format(p=IPV4))

    if ipv4.match(IP):
        return "IPv4"

    IPV6 = '([0-9a-f]{1,4})'

    ipv6 = \
       re.compile(r'^({p}\:){{7}}{p}$'.format(p=IPV6),
                  re.IGNORECASE)

    if ipv6.match(IP):
        return "IPv6"

    return "Neither"

def main():
    for index, input_string in tests.items():
        res = validIPAddress(input_string)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()