def string_end(strng, n):
    stack = list(strng)
    results =[]
    # implement this
    for i in range(n):
        result = stack.pop()
        results.append(result)
        
    return ''.join(results)

print(string_end("ijkshgegassem tnatropmi", 17))  # Expected output: important message
print(string_end("ffsfatad", 4))  # Expected output: data
print(string_end("IA", 2))  # Expected output: AI
