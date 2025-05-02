import textwrap

def wrap(string, max_width):
    c = 0
    s = ''
    for i in string:
        s += i
        c += 1
        if c == max_width:
            s += '\n'
            c=0
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)