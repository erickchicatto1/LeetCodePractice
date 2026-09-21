def evaluate_postfix_inverse(expression):
    # implement this
    findingNumbers = []
    value = expression.split(' ')
    
    for i in value:
        if i.isdigit():
            findingNumbers.append(int(i))
        else:
            #logica para los operadores
            num1 = findingNumbers.pop()
            num2 = findingNumbers.pop()
            
            if i == "-":
                operation = num1 - num2
                findingNumbers.append(operation)
            if i == "+":
                operation = num1 + num2
                findingNumbers.append(operation)
            if i == "*":
                operation = num1 * num2 
                findingNumbers.append(operation)
            if i == "/":
                operation = num1 / num2
                findingNumbers.append(operation)    
            
    return findingNumbers[0]
        
            
print(evaluate_postfix_inverse("2 3 -"))  # Expected output: 1
print(evaluate_postfix_inverse("2 3 +"))  # Expected output: 5
print(evaluate_postfix_inverse("6 3 *"))  # Expected output: 18
