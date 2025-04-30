#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n<=100 and n>=1):
    def p(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    if n!=2 and p(n) == True:
        print("Weird")
    else:
        if(n%3==0 and n%2!=0):
            print("Weird")
        elif((n%3!=0 and n%2==0 and n>=2 and n<=5 ) or (n%2==0 and n%3==0 and n>=2 and n<=5)):
            print("Not Weird")
        elif((n%3!=0 and n%2==0 and n>=6 and n<=20) or (n%2==0 and n%3==0 and n>=6 and n<=20)):
            print("Weird")
        elif((n%3!=0 and n%2==0 and n>20) or (n%2==0 and n%3==0 and n>20)):
            print("Not Weird")
        
