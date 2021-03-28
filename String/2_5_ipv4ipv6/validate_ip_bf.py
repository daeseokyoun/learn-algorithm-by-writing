from typing import List

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

def check_ip_v4(ipv4: str) -> str:
    ipnums = ipv4.split('.')

    for num in ipnums:
        if len(num) == 0 or len(num) > 3:
            return 'Neither'

        if (len(num) != 1 and num[0] == '0') or \
            not num.isdigit() or int(num) > 255:
            return 'Neither'
    return 'IPv4'

import string
def check_ip_v6(ipv6: str) -> str:
    ipnums = ipv6.split(':')

    for num in ipnums:
        if len(num) == 0 or len(num) > 4 or \
            not all(c in string.hexdigits for c in num):
            return 'Neither'
    return 'IPv6'

def validIPAddress(IP: str) -> str:
    if IP.count('.') == 3:
        return check_ip_v4(IP)
    elif IP.count(':') == 7:
        return check_ip_v6(IP)

    return 'Neither'

def main():
    for index, input_string in tests.items():
        res = validIPAddress(input_string)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()