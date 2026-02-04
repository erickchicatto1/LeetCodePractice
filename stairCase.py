import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    counter = 0
    
    for i in range(n):
        print(f"#" ,i)
        counter = counter + 1
        for j in range(counter):
            print(f"#")
 
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
