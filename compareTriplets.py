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
    # Write your code here
    scoreAlice = 0
    scoreBob = 0
    
    for i,j in a,b:
        if a[i] > b[j]:
            print("Alice awarded 1 point") 
        elif a[i] < b[j]:
            print("Bob is awarded 1 point")
        elif a[i] == b[j]:
            print("neither person receives a point")
        else:
            print("Nothing happen")
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
