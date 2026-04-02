def missingNumbers(arr, brr):
    frecuencyArr = {}
    frecuencyBrr = {}
    missingValues = []

    for value in arr:
        frecuencyArr[value] = frecuencyArr.get(value, 0) + 1

    for value in brr:
        frecuencyBrr[value] = frecuencyBrr.get(value, 0) + 1

    for key in frecuencyBrr:
        if frecuencyBrr[key] > frecuencyArr.get(key, 0):
            missingValues.append(key)

    return sorted(missingValues)
    
