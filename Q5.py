# # Problem Statement: Grade Band AnalysisYou are given the marks of $N$ students. 
# # Assign each student a grade based on their marks according to the following ranges:
# # 90–100: A
# # 80–89: B
# # 70–79: C
# # 60–69: D
# # 50–59: E
# # 0–49: F
# # <0 or >100: X (Invalid)
# # Your tasks are to:
# # Count the number of students in each grade band.
# # Print the grade band that has the maximum number of students.
# # Rules:If all students have invalid marks, print X.
# # If multiple bands have the same maximum count, print the band with the highest priority based on this order: A > B > C > D > E > F > X.

# Input Format:
# First line: An integer $N$ (the number of students).
# Second line: $N$ space-separated integers (the marks obtained by each student).

n=int(input())
marks=list(map(int,input().strip().split()))
grade_count={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'X':0}
for mark in marks:
    if 90<=mark<=100:
        grade_count['A']+=1
    elif 80<=mark<=89:
        grade_count['B']+=1
    elif 70<=mark<=79:
        grade_count['C']+=1
    elif 60<=mark<=69:
        grade_count['D']+=1
    elif 50<=mark<=59:
        grade_count['E']+=1
    elif 0<=mark<=49:
        grade_count['F']+=1
    else:
        grade_count['X']+=1
if grade_count['X'] == n:
    print('X')
else:
    # Priority order for tie-breaking
    priority = ['A', 'B', 'C', 'D', 'E', 'F', 'X']
    max_count = -1
    best_grade = ''
    
    for grade in priority:
        if grade_count[grade] > max_count:
            max_count = grade_count[grade]
            best_grade = grade
            
    print(best_grade)
