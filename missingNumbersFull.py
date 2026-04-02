def missingNumbers(arr, brr):
    # Write your code here
    frecuencyArr = {} #key - value
    frecuencyBrr = {} #key - value
    missingValues = []
    
    
    for num in arr:
        if num in frecuencyArr:
            frecuencyArr[num] += 1
        else:
            frecuencyArr[num] = 1
            
    for num in brr:
        if num in frecuencyBrr:
            frecuencyBrr[num] += 1
        else:
            frecuencyBrr[num] = 1
            
    #Compare the 2 dictionaries
    for key in frecuencyArr:
        if key not in frecuencyBrr or frecuencyArr[key] != frecuencyBrr[key]:
            missingValues.append(key)
    
    return missingValues        
            

if __name__ == '__main__':
    
    A= [203,204,205,206,207,208,203,204,205,206]
    B= [203,204,204,205,206,207,205,208,203,206,205,206,204]
    
    missingNumbers(A,B)

    #output : [204,205,206]
