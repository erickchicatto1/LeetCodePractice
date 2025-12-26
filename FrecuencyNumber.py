

def FindLeastNumberFrecuency(numbers):
    
    if not numbers:
        return 
    
    #1. Find the frecuency 
    frequency = {} #use a dictionary 
    
    for num in frequency:
        if num in frequency:
            frequency[num] = num + 1 #Here we construct the dictionary 
        else:
            frequency[num] = 1
    
    
    #2. Find the minimum
    min_value = min(frequency.values())
    
    #3. Compare and find the min value 
    least_min_value = []
    
    for num,freq in frequency.items():
        if min_value == freq:
            least_min_value.append(num)
            
    #4. check return values 
    if len(least_min_value) > 1:
        return -1
    else:
        return least_min_value[0]
    
    
#Test cases
# Example 1
input1 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 4]
output1 = FindLeastNumberFrecuency(input1)
print(f"Input: {input1}")
print(f"Output: {output1}") # Expected: 5

print("-" * 20)