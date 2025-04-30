if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    li = list(arr)
    #reverse sorting
    rli = sorted(li, reverse = True)
    #adding constrained 
    s = 0
    for i in range (0,len(rli)-1):
        if(rli[i]>=-100 and rli[i+1]<=100):
            s=0
        else:
            s=1
            break
    if(n>=2 and n<=10 and s==0):
        for i in range(0,len(rli)-1):
            if(rli[i]==rli[i+1]):
                continue
            else:
                break
        print(rli[i+1])
    
   
    
   
            
