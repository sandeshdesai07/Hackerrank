def swap_case(s):
    if 0<len(s) and len(s)<=1000:
        
        return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)