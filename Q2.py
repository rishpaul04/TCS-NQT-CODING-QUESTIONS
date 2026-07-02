# Question 2: Find Last Student ID Based on Score Frequency
# Problem Statement:You are given the student ID and the corresponding score of $N$ students.
# You are also given a target score X and a required frequency K.Logic: Count how many times the score X appears in the input.
# Condition: * If the frequency of X is greater than or equal to K, print the last student ID that had the score X.
# If the frequency of X is less than K, print -1.

# Input Format:First line contains integer N.
# Next $N$ lines contain the Student ID and Score (each line represents one student).
# Next line contains integer X (the score to check).
# Last line contains integer K (the required frequency).

n=int(input())
students=[]
for i in range(n):
    student_id,score=input().strip().split()
    students.append((student_id,int(score)))
x=int(input())
k=int(input())
count=0
last_student_id=-1
for student_id,score in students:
    if score==x:
        count+=1
        last_student_id=student_id
if count>=k:
    print(last_student_id)
else:
    print(-1)
    
