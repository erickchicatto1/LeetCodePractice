def miniMaxSum(arr):

    ValuesOfTheSum = []
    toSum = 0
    maxVal,minVal = 0,0
    
    for i in arr:
        if i == 0:
            continue
        toSum = toSum + i
        
    ValuesOfTheSum.append(toSum)
        
    return ValuesOfTheSum
    
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    miniMaxSum(arr)
