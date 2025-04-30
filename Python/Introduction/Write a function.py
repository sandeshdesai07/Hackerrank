def is_leap(year):
    leap = False
    if year%100 == 00:
        if year%400 == 00:
            return True
        return False
    else:
        if year % 4 == 0:
            return True
        return False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
