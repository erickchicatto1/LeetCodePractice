import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
userInput = input()

if(re.search(pattern,userInput)):
    print("ValidEmail")
else:
    print("inavlid Email")
