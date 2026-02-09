def birthdayCakeCandles(candles):
    # Write your code here
    maxVal = 0
    counter = 0 #to count how many numbers are repeated
    
    for x in candles:
        
        if x > maxVal:
            maxVal = x
            counter = 1
        elif x == maxVal:
            counter += 1
    return counter
        
