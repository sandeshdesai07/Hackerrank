if __name__ == '__main__':
    n = int(input())
    if (n>=1 and n<=150):
        l = []
        for i in range (1,n+1):
            l.append(i)
        st = ''.join(map(str,l))
        print(st)
