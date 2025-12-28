
def FindLeastNumberFrecuency(numbers):    
    
    if not numbers:
        return None
    
    frecuency = {} #key , value
    
    for num in numbers:
        if num in frecuency:
            frecuency[num] += 1 #key 
        else:
            frecuency[num] = 1
    
    min_freq = min(frecuency.values())
    
    candidates = []
    
    for num,freq in frecuency.items():
        if freq == min_freq:
            candidates.append(num)
    
    if len(candidates) > 1:
        return -1
    else:
        return candidates[0]
            
            
input1 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 4]
print(f"Output: {FindLeastNumberFrecuency(input1)}")