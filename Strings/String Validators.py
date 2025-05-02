if __name__ == '__main__':
    s = input()
    import re
    pattern1 = r'[a-zA-Z0-9]+'
    pattern2 = r'[a-zA-Z]+'
    pattern3 = r'[0-9]+'
    pattern4 = r'[a-z]+'
    pattern5 = r'[A-Z]+'
    print(bool(re.search(pattern1,s)))
    print(bool(re.search(pattern2,s)))
    print(bool(re.search(pattern3,s)))
    print(bool(re.search(pattern4,s)))
    print(bool(re.search(pattern5,s)))
