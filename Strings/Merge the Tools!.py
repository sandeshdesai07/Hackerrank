def merge_the_tools(string, k):
    n = len(string)
    if (1<=n) and (n<=10**4) and (1<=k) and (k<=n) and not (n%k):
        for i in range(0,n,k):
            sbtr = string[i:i+k]
            s = set()
            result = ''
            for char in sbtr:
                if char not in s:
                    s.add(char)
                    result += char
            print(result)

        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)