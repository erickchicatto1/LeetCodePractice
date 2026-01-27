def diagonalReference(arr):
    ltr_diag = rtl_diag = 0
    
    for i in range(len(arr)):
        ltr_diag += arr[i][i]
        rtl_diag += arr[i][len(arr)-1-i]
    return abs(ltr_diag-rtl_diag )
    


if __name__ == "__main__":
    
    matrix = [
        [11,2,4],
        [4,5,6],
        [10,8,-12]
    ]
    
    resultado = diagonalReference(matrix)