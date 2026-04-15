




if __name__ == "__main__":
    
    
    student_marks = {} #key:value
    n = int(input())
    
    #1. save into the dict student_marks
    for i in n:
        student_marks[i]=n
    #2. Sum the values
    for i in student_marks.items():
        student_marks[i] += (student_marks[i] + student_marks[i] + student_marks[i]) / 3
    #3. Select the minimum values , how to make for a dict?
    val_min = min(student_marks)
    
    
    #show the values that are already saved , how to use this?
    for idx in range(n):
        name , *line = input().split() #*line takes the other part of the split
        scores = list(map(float,line))
        student_marks[name] = scores
    
    query_name = input()
    
    
