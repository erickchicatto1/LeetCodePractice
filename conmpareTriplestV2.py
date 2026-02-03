#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
    scoreAlice = 0 
    scoreBob = 0
    
    for val_a,val_b in zip(a,b):
        if val_a > val_b:
            scoreAlice += 1
        elif val_a < val_b:
            scoreBob += 1
    return [scoreAlice,scoreBob]
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
