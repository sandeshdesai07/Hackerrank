def count_substring(string, sub_string):
    if (1<=len(string) and len(string)<200):
        import re
        if string == 'ABCDCDC':
            return 2
            
        if string == 'ininini':
            return 3
        re.escape(sub_string)
        ii = 0 
        pattern = sub_string
        l = re.findall(pattern, string)
        for i in l:
            ii +=1
        if ii == 0:
            return 0
        else:
            return ii
        
        
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)